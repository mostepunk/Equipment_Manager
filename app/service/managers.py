from tool import Tool
from construction import Construction
from worker import Worker
from my_exception import checking_incoming_objects, checking_fields_filled


class ToolManager():
    '''
    Менеджер инструмента
    '''

    def __init__(self, tool: Tool) -> None:
        if type(tool)!=Tool:
            raise TypeError("Передан неиспользуемый класс")
        self.tool = tool


    def filling_fields (self, construction:Construction, responsible:Worker) -> None:
        '''
        Первоначальное заполненние полей инструмента.
        Другие методы по измененнию полей и зависимостей
        не будут работать до вызова этого метода
        '''
        # Проверка передаваемых значений
        checking_incoming_objects(self.filling_fields.__annotations__, [construction, responsible])
        
        self.tool.change_construction(construction)
        self.tool.change_responsible(responsible)

        # Добавление этого инструмента на объект и к ответственному лицу
        construction.add_tool(self)
        responsible.add_tool(self)

        
    def set_construction(self, new_construction:Construction) -> None:
        '''
        Изменение объекта,
        на котором находится инструмент
        '''
        # Проверка на заполненность полей
        checking_fields_filled([self.tool.get_responsible, self.tool.get_construction])
        # Проверка передаваемых значений
        checking_incoming_objects(self.set_construction.__annotations__, [new_construction])
        
        # Если новый объект не тот же что и текущий, то выполняем инструкции
        if new_construction!=self.tool.get_construction():
        
            # удаление из списка инструментов в старом объекте
            self.tool.get_construction().delete_tool(self)
            # добавление в список инструментов в новый объект
            new_construction.add_tool(self)
            # смена объекта у инструмента
            self.tool.change_construction(new_construction)
            # удаление из списка инструментов прошлого ответственного
            self.tool.get_responsible().delete_tool(self)
            # смена ответственного лица у инструмента
            self.tool.change_responsible(new_construction.get_responsible())
            # добавление в список инструментов к новому ответственному
            new_construction.get_responsible().add_tool(self)
        

    def set_responsible(self, new_responsible:Worker) -> None:
        '''
        Изменение ответственного,
        в подчинении у которого
        находится инструмент
        '''
        # Проверка на заполненность полей
        checking_fields_filled([self.tool.get_responsible, self.tool.get_construction])
        # Проверка передаваемых значений
        checking_incoming_objects(self.set_responsible.__annotations__, [new_responsible])

        # Если новый ответственный не тот же что и текущий, то выполняем инструкции
        if new_responsible!=self.tool.get_responsible():
            
            # Удаление из списка инструментов у текущего ответственного
            self.tool.get_responsible().delete_tool(self)
            # Добавление в список инструментов к новому ответственному
            new_responsible.add_tool(self)
            # Смена ответственного лица
            self.tool.change_responsible(new_responsible)
            # Удаление из списка инструментов у текущего объекта
            self.tool.get_construction().delete_tool(self)
            # Смена объекта
            self.tool.change_construction(new_responsible.get_construction())
            # Добавление в список инструментов в новом объекте
            self.tool.get_construction().add_tool(self)


class WorkerManager():
    '''
    Менеджер работников
    '''

    def __init__(self, worker: Worker) -> None:
        if type(worker)!=Worker:
            raise TypeError("Передан неиспользуемый класс")
        self.worker = worker


    def set_construction(self, construction:Construction) -> None:
        '''
        Изменение поля с объектом
        '''
        # Проверка передаваемых значений
        checking_incoming_objects(self.set_construction.__annotations__, [construction])

        self.worker.change_construction(construction)


class ConstructionManager():
    '''
    Менеджер работников
    '''

    def __init__(self, construction: Construction) -> None:
        if type(construction)!=Construction:
            raise TypeError("Передан неиспользуемый класс")
        self.construction = construction


    def set_responsible(self, responsible:Worker) -> None:
        '''
        Изменение поля с ответственным
        '''

        # Проверка передаваемых значений
        checking_incoming_objects(self.set_responsible.__annotations__, [responsible])

        self.construction.change_responsible(responsible)
        


