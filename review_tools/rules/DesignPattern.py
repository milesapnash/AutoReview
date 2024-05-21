from review_tools.rules.Design import StrategyPattern, TemplateMethodPattern, \
    SingletonPattern

pattern_dict = {'template': TemplateMethodPattern, 'strategy': StrategyPattern,
                'singleton': SingletonPattern}


def find_pattern(pattern, project):
    return pattern_dict[pattern].find_pattern(project.files)