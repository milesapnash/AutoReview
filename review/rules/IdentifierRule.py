from review.filters.Filter import get_node_name
from review.rules.Rule import Rule


# Checks that all nodes within scope follow naming convention
class IdentifierRule(Rule):
    def __init__(self, scope='project', node_filter=None):
        super().__init__(scope)
        self.node_filter = node_filter

    def apply(self, file):
        ast = self.file_filter(file)
        if ast is None or self.node_filter is None:
            return []

        feedback = []
        for node in self.node_filter.get_nodes(ast):
            line, char = node.position
            name = get_node_name(node, 'java')
            feedback.append(
                f'{file.file_name}:{line}:{char}: The {self.node_filter.node_class}, '
                f'{name}, does not follow the specified naming convention.')

        return feedback
