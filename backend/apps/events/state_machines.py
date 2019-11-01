from apps.events import constants as cts


class EventStateMachine:
    TRANSITIONS = {
        cts.ACTIVE: {cts.CANCELED}
    }


class MembershipStateMachine:
    TRANSITIONS = {
        cts.INITIAL: {cts.CANCELED, cts.PAID},
        cts.PAID: {cts.CANCELED},
    }
