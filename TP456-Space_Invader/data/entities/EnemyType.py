"""
Class permettant l'identification des enemies grace à des enum.
Date : 12/12/2022
Florian Trémouille et Hugo Miaglia
"""

from enum import Enum

class EnemyType(Enum):
    BasicEnemy = 'basic_enemy'
    AdvancedEnemy = 'advanced_enemy'
    BossEnemy = 'boss_enemy'