
class BaseLogic:
    """Base class for logic operations."""

    # Encapsulation
    def _check_type(self, value, expected_type):
        """Helper method for checking type."""
        if not isinstance(value, expected_type):
            raise TypeError(
                f'Expected type: {expected_type}, received {type(value)}')
        return True


# Inheritance
class LogicChecker(BaseLogic):
    """A class realizing all basic logical operations and validations."""

    def and_operation(self, a: bool, b: bool) -> bool:
        """Logical AND (conjunction) for two arguments."""
        self._check_type(a, bool)
        self._check_type(b, bool)
        return a and b

    def or_operation(self, a: bool, b: bool) -> bool:
        """Logical OR (disjunction) for two arguments."""
        self._check_type(a, bool)
        self._check_type(b, bool)
        return a or b

    def not_operation(self, a: bool) -> bool:
        """Logical NOT (negation) for one argument."""
        self._check_type(a, bool)
        return not a

    def implication(self, a: bool, b: bool) -> bool:
        """IMPLICATION operation for two arguments."""
        self._check_type(a, bool)
        self._check_type(a, bool)
        return not a or b

    def equivalence(self, a: bool, b: bool) -> bool:
        """EQUIVALENCE operation for two arguments."""
        self._check_type(a, bool)
        self._check_type(a, bool)
        return a == b

    def xor_operation(self, a: bool, b: bool) -> bool:
        """Exclusive OR operation (logical XOR) for two arguments."""
        self._check_type(a, bool)
        self._check_type(b, bool)
        return (a or b) and not (a and b)

    def nand_operation(self, a: bool, b: bool) -> bool:
        """NOT AND operation for two arguments."""
        self._check_type(a, bool)
        self._check_type(b, bool)
        return not (a and b)

    def nor_operation(self, a: bool, b: bool) -> bool:
        """NOT OR operation for two arguments."""
        self._check_type(a, bool)
        self._check_type(b, bool)
        return not (a or b)
