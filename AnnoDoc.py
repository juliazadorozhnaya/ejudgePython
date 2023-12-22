"""
Написать декоратор annodoc(), которым можно декорировать классы и функции. Декоратор должен просматривать аннотации объекта и
выбирать из них только такие, у которых вместо типа в аннотации используется строка. Эти строки (если они есть) надо добавлять в
документацию объекта так: (всегда) В начало строки документации — имя: (где имя — это поле .__name__ объекта) ⇒ Если у объекта не
было строки документации, она создаётся В конец строки документации — Variable имя: аннотация-строка (поля класса,
формальные параметры функции или метода) В самый конец строки документации — Returns: аннотация-строка для возвращаемого значения
Аннотированный объект следует просмотреть рекурсивно, и для каждого аннотированного указанным способом атрибута изменить
 строку документации с помощью annodoc(). Гарантируется, что в тестах эта рекурсия конечна.
"""

import inspect

def annodoc(cls):
    def add_annotations(doc, annotations):
        lines = [doc] if doc else []
        for name, annotation in annotations.items():
            if isinstance(annotation, str):
                if name == 'return':
                    lines.append(f'Returns: {annotation}')  # Handling return annotation separately
                else:
                    lines.append(f'Variable {name}: {annotation}')
        return '\n'.join(lines)

    def update_doc(obj):
        existing_doc = obj.__doc__.strip() if obj.__doc__ else ''
        doc = f'{obj.__name__}:\n{existing_doc}' if existing_doc else f'{obj.__name__}:'
        annotations = getattr(obj, '__annotations__', {})
        obj.__doc__ = add_annotations(doc, annotations)

        for name, member in obj.__dict__.items():
            if inspect.isfunction(member) or inspect.isclass(member):
                update_doc(member)

    update_doc(cls)
    return cls

