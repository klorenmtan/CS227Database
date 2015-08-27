
# C:\Users\Gladys Tillan\Documents\GitHub\parser\parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = 'AB551F67D5F175A6FA29C6DD8444E097'
    
_lr_action_items = {'INT':([22,24,29,31,39,44,48,49,50,51,52,53,54,73,75,79,80,88,],[32,32,32,32,32,32,-33,-35,32,-34,-36,32,32,32,32,32,32,32,]),'ON':([43,],[59,]),'AND':([32,33,34,35,36,38,40,41,46,56,60,63,64,65,66,73,75,79,80,88,],[-41,-31,-39,-40,-42,54,-43,54,54,54,54,-32,54,-29,-30,79,79,79,79,79,]),'ID':([2,5,13,14,15,16,22,24,26,29,39,42,44,48,49,50,51,52,53,54,59,62,71,72,73,75,79,80,81,87,88,],[10,12,17,10,19,10,34,34,43,34,34,58,34,-33,-35,34,-34,-36,34,34,68,10,73,74,34,34,34,34,85,88,34,]),'SET':([12,],[16,]),'$end':([1,3,4,6,23,28,30,45,55,57,61,69,],[-2,-3,0,-1,-10,-6,-4,-7,-11,-8,-5,-9,]),'DOUBLE':([22,24,29,31,39,44,48,49,50,51,52,53,54,73,75,79,80,88,],[36,36,36,36,36,36,-33,-35,36,-34,-36,36,36,36,36,36,36,36,]),'SELECT':([0,],[2,]),'FROM':([7,8,9,10,11,19,],[13,14,-12,-37,-13,-38,]),'GT':([32,34,35,36,37,40,],[-41,-39,-40,-42,49,-43,]),'STRING':([22,24,29,31,39,44,48,49,50,51,52,53,54,73,75,79,80,88,],[40,40,40,40,40,40,-33,-35,40,-34,-36,40,40,40,40,40,40,40,]),'UPDATE':([0,],[5,]),'LPAREN':([22,24,29,39,44,53,54,73,75,79,80,88,],[39,39,39,39,39,39,39,80,80,80,80,80,]),'LT':([32,34,35,36,37,40,],[-41,-39,-40,-42,52,-43,]),'WHERE':([10,17,18,19,20,27,32,34,35,36,40,47,58,63,67,70,73,76,77,78,82,83,86,88,89,90,],[-37,22,24,-38,29,44,-41,-39,-40,-42,-43,-14,-16,-32,-17,-15,-18,-27,-19,-20,-25,-24,-26,-21,-22,-23,]),'COMMA':([10,11,18,19,21,32,36,40,47,],[-37,15,15,-38,15,-41,-42,-43,62,]),'NATURAL':([10,18,19,58,73,88,],[-37,25,-38,25,25,25,]),'NEQ':([32,34,35,36,37,40,],[-41,-39,-40,-42,51,-43,]),'JOIN':([10,18,19,25,58,73,88,],[-37,26,-38,42,26,26,26,]),'DOT':([68,85,],[72,87,]),'EQ':([10,19,21,32,34,35,36,37,40,68,74,],[-37,-38,31,-41,-39,-40,-42,48,-43,71,81,]),'OR':([32,33,34,35,36,38,40,41,46,56,60,63,64,65,66,73,75,79,80,88,],[-41,-31,-39,-40,-42,53,-43,53,53,53,53,-32,-28,-29,-30,75,75,75,75,75,]),'ALL':([2,],[9,]),'RPAREN':([32,33,34,35,36,40,56,63,64,65,66,76,82,83,84,86,],[-41,-31,-39,-40,-42,-43,66,-32,-28,-29,-30,-27,-25,-24,86,-26,]),'EOL':([10,17,18,19,20,27,32,33,34,35,36,38,40,41,46,47,58,60,63,64,65,66,67,70,73,76,77,78,82,83,86,88,89,90,],[-37,23,28,-38,30,45,-41,-31,-39,-40,-42,55,-43,57,61,-14,-16,69,-32,-28,-29,-30,-17,-15,-18,-27,-19,-20,-25,-24,-26,-21,-22,-23,]),'DELETE':([0,],[7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'select_statement':([0,],[1,]),'comp_op':([37,],[50,]),'id_list':([2,14,16,62,],[11,18,21,21,]),'comparison_predicate':([22,24,29,39,44,53,54,73,75,79,80,88,],[33,33,33,33,33,33,33,76,76,76,76,76,]),'statement':([0,],[4,]),'literal':([22,24,29,31,39,44,50,53,54,73,75,79,80,88,],[35,35,35,47,35,35,35,35,35,35,35,35,35,35,]),'delete_statement':([0,],[3,]),'value':([22,24,29,39,44,50,53,54,73,75,79,80,88,],[37,37,37,37,37,63,37,37,37,37,37,37,37,]),'join_clause':([18,58,73,88,],[27,67,77,89,]),'select_columns':([2,],[8,]),'update_statement':([0,],[6,]),'join_search_condition':([73,75,79,80,88,],[78,82,83,84,90,]),'set_clause_list':([16,62,],[20,70,]),'search_condition':([22,24,29,39,44,53,54,],[38,41,46,56,60,64,65,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> update_statement','statement',1,'p_statement','update_select_delete.py',97),
  ('statement -> select_statement','statement',1,'p_statement','update_select_delete.py',98),
  ('statement -> delete_statement','statement',1,'p_statement','update_select_delete.py',99),
  ('update_statement -> UPDATE ID SET set_clause_list EOL','update_statement',5,'p_update_statement','update_select_delete.py',104),
  ('update_statement -> UPDATE ID SET set_clause_list WHERE search_condition EOL','update_statement',7,'p_update_statement','update_select_delete.py',105),
  ('select_statement -> SELECT select_columns FROM id_list EOL','select_statement',5,'p_select_statement','update_select_delete.py',113),
  ('select_statement -> SELECT select_columns FROM id_list join_clause EOL','select_statement',6,'p_select_statement','update_select_delete.py',114),
  ('select_statement -> SELECT select_columns FROM id_list WHERE search_condition EOL','select_statement',7,'p_select_statement','update_select_delete.py',115),
  ('select_statement -> SELECT select_columns FROM id_list join_clause WHERE search_condition EOL','select_statement',8,'p_select_statement','update_select_delete.py',116),
  ('delete_statement -> DELETE FROM ID EOL','delete_statement',4,'p_delete_statement','update_select_delete.py',128),
  ('delete_statement -> DELETE FROM ID WHERE search_condition EOL','delete_statement',6,'p_delete_statement','update_select_delete.py',129),
  ('select_columns -> ALL','select_columns',1,'p_select_columns','update_select_delete.py',137),
  ('select_columns -> id_list','select_columns',1,'p_select_columns','update_select_delete.py',138),
  ('set_clause_list -> id_list EQ literal','set_clause_list',3,'p_set_clause_list','update_select_delete.py',143),
  ('set_clause_list -> id_list EQ literal COMMA set_clause_list','set_clause_list',5,'p_set_clause_list','update_select_delete.py',144),
  ('join_clause -> NATURAL JOIN ID','join_clause',3,'p_join_clause','update_select_delete.py',152),
  ('join_clause -> NATURAL JOIN ID join_clause','join_clause',4,'p_join_clause','update_select_delete.py',153),
  ('join_clause -> JOIN ID ON ID EQ ID','join_clause',6,'p_join_clause','update_select_delete.py',154),
  ('join_clause -> JOIN ID ON ID EQ ID join_clause','join_clause',7,'p_join_clause','update_select_delete.py',155),
  ('join_clause -> JOIN ID ON ID EQ ID join_search_condition','join_clause',7,'p_join_clause','update_select_delete.py',156),
  ('join_clause -> JOIN ID ON ID DOT ID EQ ID DOT ID','join_clause',10,'p_join_clause','update_select_delete.py',157),
  ('join_clause -> JOIN ID ON ID DOT ID EQ ID DOT ID join_clause','join_clause',11,'p_join_clause','update_select_delete.py',158),
  ('join_clause -> JOIN ID ON ID DOT ID EQ ID DOT ID join_search_condition','join_clause',11,'p_join_clause','update_select_delete.py',159),
  ('join_search_condition -> AND join_search_condition','join_search_condition',2,'p_join_search_condition','update_select_delete.py',175),
  ('join_search_condition -> OR join_search_condition','join_search_condition',2,'p_join_search_condition','update_select_delete.py',176),
  ('join_search_condition -> LPAREN join_search_condition RPAREN','join_search_condition',3,'p_join_search_condition','update_select_delete.py',177),
  ('join_search_condition -> comparison_predicate','join_search_condition',1,'p_join_search_condition','update_select_delete.py',178),
  ('search_condition -> search_condition OR search_condition','search_condition',3,'p_search_condition','update_select_delete.py',188),
  ('search_condition -> search_condition AND search_condition','search_condition',3,'p_search_condition','update_select_delete.py',189),
  ('search_condition -> LPAREN search_condition RPAREN','search_condition',3,'p_search_condition','update_select_delete.py',190),
  ('search_condition -> comparison_predicate','search_condition',1,'p_search_condition','update_select_delete.py',191),
  ('comparison_predicate -> value comp_op value','comparison_predicate',3,'p_comparison_predicate','update_select_delete.py',202),
  ('comp_op -> EQ','comp_op',1,'p_comp_op','update_select_delete.py',207),
  ('comp_op -> NEQ','comp_op',1,'p_comp_op','update_select_delete.py',208),
  ('comp_op -> GT','comp_op',1,'p_comp_op','update_select_delete.py',209),
  ('comp_op -> LT','comp_op',1,'p_comp_op','update_select_delete.py',210),
  ('id_list -> ID','id_list',1,'p_id_list','update_select_delete.py',215),
  ('id_list -> id_list COMMA ID','id_list',3,'p_id_list','update_select_delete.py',216),
  ('value -> ID','value',1,'p_value','update_select_delete.py',224),
  ('value -> literal','value',1,'p_value','update_select_delete.py',225),
  ('literal -> INT','literal',1,'p_literal','update_select_delete.py',230),
  ('literal -> DOUBLE','literal',1,'p_literal','update_select_delete.py',231),
  ('literal -> STRING','literal',1,'p_literal','update_select_delete.py',232),
]
