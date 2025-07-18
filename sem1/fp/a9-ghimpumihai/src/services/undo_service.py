# src/services/undo_service.py
class FunctionCall:
    def __init__(self, function, *parameters):
        self._function = function
        self._parameters = parameters

    def call(self):
        self._function(*self._parameters)

class Operation:
    def __init__(self, undo_function_call, redo_function_call):
        self._undo_function_call = undo_function_call
        self._redo_function_call = redo_function_call

    def undo(self):
        self._undo_function_call.call()

    def redo(self):
        self._redo_function_call.call()

class CascadingOperation:
    def __init__(self):
        self._operations = []

    def add_operation(self, operation):
        self._operations.append(operation)

    def undo(self):
        for operation in reversed(self._operations):
            operation.undo()

    def redo(self):
        for operation in self._operations:
            operation.redo()

class UndoService:
    def __init__(self):
        self._history = []
        self._redo_stack = []

    def record(self, operation):
        self._history.append(operation)
        self._redo_stack.clear()

    def undo(self):
        if self._history:
            operation = self._history.pop()
            operation.undo()
            self._redo_stack.append(operation)

    def redo(self):
        if self._redo_stack:
            operation = self._redo_stack.pop()
            operation.redo()
            self._history.append(operation)