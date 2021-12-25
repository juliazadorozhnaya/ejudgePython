class Tester:
    def __init__(self, func):
        self.func = func

    def __call__(self, suites, allowed=[], **kwargs):
        errors = []
        for suite in suites:
            try:
                self.func(*suite)
            except Exception as e:
                errors.append(e)
        if not errors:
            return 0
        return -1 if all(
            type(
                error
            ) in allowed or Exception in allowed for error in errors) else 1

