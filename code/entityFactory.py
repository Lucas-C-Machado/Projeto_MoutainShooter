#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background


class EntityFactory:

    @staticmethod #método estático
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7): #7 backgrounds ao todo
                    list_bg.append(Background(f'Level1Bg{i}', position(0, 0))) #vai passando os níveis e juntando TODOS os backgrounds
                return list_bg

