# -*- coding: utf-8 -*-
import logging
from contextlib import suppress

from apps.state_machine.exceptions import StopStateChange, WrongState

logger = logging.getLogger(__name__)


class FiniteStateMachineMixin(object):
    """Mixins which adds the behavior of a state_machine."""

    # Represents the state machine for the object
    # The states and transitions should be specified.
    # {
    #    'pending': next_states_tuples or '__all__'
    # }
    state_machine = None
    class_history = None
    deprecated_states = None

    def get_state(self):
        return self.state or None

    def get_states_to_change(self):
        """
        Returns a collection with a list of possible states that
        Product can change without raise an exception
        """
        states_to_change = []
        states = self.get_valid_transitions()
        for state in states:
            verbose_state = self.get_verbose_state()
            states_to_change.append((state, verbose_state))
        return states_to_change

    def can_change(self, next_state):
        """Validates if the next_state can be executed or not.

        It uses the state_machine attribute in the class.
        """
        valid_transitions = self.get_valid_transitions()

        if not valid_transitions:
            return False

        return next_state in valid_transitions

    def get_valid_transitions(self):
        """Return possible states to whom a product can transition.

        @return {tuple/list}
        """
        current = self.get_state()
        valid_transitions = self.state_machine.get(current)

        if valid_transitions == '__all__':
            return list(self.state_machine.keys())

        return self.state_machine.get(current, ())

    def on_change_state(self, previous_state, next_state, **kwargs):
        """Called everytime an state changes.

        @param {str/int} previous_state
        @param {str/int} next_state
        Useful for catch events related with emails and others things.
        """
        pass

    def _get_previous_history_state(self):
        """
        Retorna el penúltimo estado histórico de un producto/cuota.
        Este método es privado, úselo con cautela.
        """
        query_filter = {self.class_history.parent_field_name: self}
        qs = self.class_history.objects.filter(**query_filter)
        try:
            previous_state = qs.order_by('-date', '-pk')[1].state
        except IndexError:
            raise WrongState('There is not previous_state')
        return previous_state

    def undo_state(self, auto_save=True, **kwargs):
        """Revert current state to last historic state."""
        current_state = self.get_state()
        previous_state = self._get_previous_history_state()
        if self.can_undo(previous_state):
            # record this in historic changes
            self.state = previous_state
            self.create_history()
            name = 'on_undo_{0}_callback'.format(current_state)
            callback = getattr(self, name, None)
            if callback:
                callback(**kwargs)
            if auto_save:
                self.save()
        else:
            msg = "The transition from {0} to {1} is not valid".format(current_state, previous_state)
            raise WrongState(msg)

    def can_undo(self, previous_state):
        return self.state in self.state_machine.get(previous_state, [])

    def execute_callback(self, name_format, state, auto_save, **kwargs):
        name = name_format.format(state)
        callback = getattr(self, name, None)
        if callback:
            kwargs.update({'auto_save': auto_save})
            callback(**kwargs)

    def change_state(self, next_state, auto_save=True,
                     ignore_before_callback=False, ignore_on_callback=False,
                     force_change=False, **kwargs):
        """Performs a transition from current state to next state if possible.

        @param {str/int} next_state
        """
        current_state = self.get_state()
        if force_change:
            msg = 'Change state executed with force_change=True'
            logger.warning(msg)

        if self.can_change(next_state) or force_change:
            with suppress(StopStateChange):
                if not ignore_before_callback:
                    self.execute_callback(
                        'on_before_{0}_callback', next_state, auto_save, **kwargs)

                self.state = next_state
                self.create_history(**kwargs)
                self.on_change_state(current_state, next_state, **kwargs)
                if auto_save:
                    self.save()
                    # This was added because in some cases, a Model is instanciated
                    # but not saved, and there are some operations that require
                    # the existance of the instance.
                if not ignore_on_callback:
                    self.execute_callback(
                        'on_{0}_callback', next_state, auto_save, **kwargs)
        else:
            msg = "The transition from {0} to {1} is not valid".format(current_state, next_state)
            raise WrongState(msg)

    def create_history(self, **kwargs):
        params = {
            self.class_history.parent_field_name: self,
            'state': kwargs.get('state') or self.state,
            'reason': kwargs.get('reason'),
        }

        self.class_history.objects.create(**params)
