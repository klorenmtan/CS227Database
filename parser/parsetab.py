
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = 'B9170F0376457C3CC1C08D0F7C4F586F'
    
_lr_action_items = {'$end':([1,3,4,5,19,37,40,42,46,65,69,72,74,77,81,85,86,89,92,93,],[-2,-3,-1,0,-10,-4,-8,-6,-11,-5,-7,-18,-9,-23,-16,-19,-20,-17,-22,-21,]),'SELECT':([0,],[7,]),'STRING':([18,25,27,29,35,36,41,47,48,49,50,51,52,53,58,79,88,],[28,28,28,28,28,28,28,28,28,-32,-33,28,-31,-34,28,28,28,]),'GT':([24,26,28,32,33,34,],[-39,-38,-41,-37,-40,50,]),'FROM':([2,10,11,12,13,22,],[8,-13,-35,17,-12,-36,]),'WHERE':([11,14,21,22,23,24,28,33,40,54,70,72,77,81,85,86,89,92,93,],[-35,18,36,-36,41,-39,-41,-40,58,-14,-15,-18,-23,-16,-19,-20,-17,-22,-21,]),'DOT':([71,84,],[75,87,]),'INT':([18,25,27,29,35,36,41,47,48,49,50,51,52,53,58,79,88,],[24,24,24,24,24,24,24,24,24,-32,-33,24,-31,-34,24,24,24,]),'EOL':([11,14,21,22,23,24,26,28,30,31,32,33,44,45,54,55,59,60,61,62,63,67,68,70,72,73,77,79,81,82,83,85,86,88,89,90,91,92,93,],[-35,19,37,-36,42,-39,-38,-41,-29,46,-37,-40,-27,-26,-14,65,69,-28,-24,-25,-30,72,74,-15,-18,77,-23,81,-16,85,86,-19,-20,89,-17,92,93,-22,-21,]),'UPDATE':([0,],[6,]),'DOUBLE':([18,25,27,29,35,36,41,47,48,49,50,51,52,53,58,79,88,],[33,33,33,33,33,33,33,33,33,-32,-33,33,-31,-34,33,33,33,]),'EQ':([11,20,22,24,26,28,32,33,34,71,78,],[-35,35,-36,-39,-38,-41,-37,-40,52,76,80,]),'DELETE':([0,],[2,]),'RPAREN':([24,26,28,30,32,33,43,44,45,60,61,62,63,],[-39,-38,-41,-29,-37,-40,60,-27,-26,-28,-24,-25,-30,]),'NATURAL':([11,22,23,67,79,88,],[-35,-36,39,39,39,39,]),'OR':([18,24,25,26,27,28,29,30,31,32,33,36,41,43,44,45,47,48,55,58,59,60,61,62,63,68,79,83,88,91,],[27,-39,27,-38,27,-41,27,-29,47,-37,-40,27,27,47,-27,-26,27,27,47,27,47,-28,-24,-25,-30,47,27,47,27,47,]),'AND':([18,24,25,26,27,28,29,30,31,32,33,36,41,43,44,45,47,48,55,58,59,60,61,62,63,68,79,83,88,91,],[29,-39,29,-38,29,-41,29,-29,48,-37,-40,29,29,48,48,-26,29,29,48,29,48,-28,48,-25,-30,48,29,48,29,48,]),'ALL':([7,],[13,]),'ON':([56,],[66,]),'NEQ':([24,26,28,32,33,34,],[-39,-38,-41,-37,-40,49,]),'COMMA':([10,11,20,22,23,24,28,33,54,],[16,-35,16,-36,16,-39,-41,-40,64,]),'ID':([6,7,8,15,16,17,18,25,27,29,36,38,41,47,48,49,50,51,52,53,57,58,64,66,75,76,79,80,87,88,],[9,11,14,11,22,11,32,32,32,32,32,56,32,32,32,-32,-33,32,-31,-34,67,32,11,71,78,79,32,84,88,32,]),'SET':([9,],[15,]),'LPAREN':([18,25,27,29,36,41,47,48,58,79,88,],[25,25,25,25,25,25,25,25,25,25,25,]),'JOIN':([11,22,23,39,67,79,88,],[-35,-36,38,57,38,38,38,]),'LT':([24,26,28,32,33,34,],[-39,-38,-41,-37,-40,53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'select_statement':([0,],[1,]),'delete_statement':([0,],[3,]),'update_statement':([0,],[4,]),'statement':([0,],[5,]),'select_columns':([7,],[12,]),'join_clause':([23,67,79,88,],[40,73,82,90,]),'comp_op':([34,],[51,]),'literal':([18,25,27,29,35,36,41,47,48,51,58,79,88,],[26,26,26,26,54,26,26,26,26,26,26,26,26,]),'id_list':([7,15,17,64,],[10,20,23,20,]),'comparison_predicate':([18,25,27,29,36,41,47,48,58,79,88,],[30,30,30,30,30,30,30,30,30,30,30,]),'set_clause_list':([15,64,],[21,70,]),'search_condition':([18,25,27,29,36,41,47,48,58,79,88,],[31,43,44,45,55,59,61,62,68,83,91,]),'value':([18,25,27,29,36,41,47,48,51,58,79,88,],[34,34,34,34,34,34,34,34,63,34,34,34,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> update_statement','statement',1,'p_statement','update_select_delete.py',96),
  ('statement -> select_statement','statement',1,'p_statement','update_select_delete.py',97),
  ('statement -> delete_statement','statement',1,'p_statement','update_select_delete.py',98),
  ('update_statement -> UPDATE ID SET set_clause_list EOL','update_statement',5,'p_update_statement','update_select_delete.py',103),
  ('update_statement -> UPDATE ID SET set_clause_list WHERE search_condition EOL','update_statement',7,'p_update_statement','update_select_delete.py',104),
  ('select_statement -> SELECT select_columns FROM id_list EOL','select_statement',5,'p_select_statement','update_select_delete.py',107),
  ('select_statement -> SELECT select_columns FROM id_list WHERE search_condition EOL','select_statement',7,'p_select_statement','update_select_delete.py',108),
  ('select_statement -> SELECT select_columns FROM id_list join_clause','select_statement',5,'p_select_statement','update_select_delete.py',109),
  ('select_statement -> SELECT select_columns FROM id_list join_clause WHERE search_condition EOL','select_statement',8,'p_select_statement','update_select_delete.py',110),
  ('delete_statement -> DELETE FROM ID EOL','delete_statement',4,'p_delete_statement','update_select_delete.py',113),
  ('delete_statement -> DELETE FROM ID WHERE search_condition EOL','delete_statement',6,'p_delete_statement','update_select_delete.py',114),
  ('select_columns -> ALL','select_columns',1,'p_select_columns','update_select_delete.py',117),
  ('select_columns -> id_list','select_columns',1,'p_select_columns','update_select_delete.py',118),
  ('set_clause_list -> id_list EQ literal','set_clause_list',3,'p_set_clause_list','update_select_delete.py',121),
  ('set_clause_list -> id_list EQ literal COMMA set_clause_list','set_clause_list',5,'p_set_clause_list','update_select_delete.py',122),
  ('join_clause -> JOIN ID ON ID EQ ID EOL','join_clause',7,'p_join_clause','update_select_delete.py',125),
  ('join_clause -> JOIN ID ON ID DOT ID EQ ID DOT ID EOL','join_clause',11,'p_join_clause','update_select_delete.py',126),
  ('join_clause -> NATURAL JOIN ID EOL','join_clause',4,'p_join_clause','update_select_delete.py',127),
  ('join_clause -> JOIN ID ON ID EQ ID join_clause EOL','join_clause',8,'p_join_clause','update_select_delete.py',128),
  ('join_clause -> JOIN ID ON ID EQ ID search_condition EOL','join_clause',8,'p_join_clause','update_select_delete.py',129),
  ('join_clause -> JOIN ID ON ID DOT ID EQ ID DOT ID search_condition EOL','join_clause',12,'p_join_clause','update_select_delete.py',130),
  ('join_clause -> JOIN ID ON ID DOT ID EQ ID DOT ID join_clause EOL','join_clause',12,'p_join_clause','update_select_delete.py',131),
  ('join_clause -> NATURAL JOIN ID join_clause EOL','join_clause',5,'p_join_clause','update_select_delete.py',132),
  ('search_condition -> search_condition OR search_condition','search_condition',3,'p_search_condition','update_select_delete.py',135),
  ('search_condition -> search_condition AND search_condition','search_condition',3,'p_search_condition','update_select_delete.py',136),
  ('search_condition -> AND search_condition','search_condition',2,'p_search_condition','update_select_delete.py',137),
  ('search_condition -> OR search_condition','search_condition',2,'p_search_condition','update_select_delete.py',138),
  ('search_condition -> LPAREN search_condition RPAREN','search_condition',3,'p_search_condition','update_select_delete.py',139),
  ('search_condition -> comparison_predicate','search_condition',1,'p_search_condition','update_select_delete.py',140),
  ('comparison_predicate -> value comp_op value','comparison_predicate',3,'p_comparison_predicate','update_select_delete.py',143),
  ('comp_op -> EQ','comp_op',1,'p_comp_op','update_select_delete.py',146),
  ('comp_op -> NEQ','comp_op',1,'p_comp_op','update_select_delete.py',147),
  ('comp_op -> GT','comp_op',1,'p_comp_op','update_select_delete.py',148),
  ('comp_op -> LT','comp_op',1,'p_comp_op','update_select_delete.py',149),
  ('id_list -> ID','id_list',1,'p_id_list','update_select_delete.py',152),
  ('id_list -> id_list COMMA ID','id_list',3,'p_id_list','update_select_delete.py',153),
  ('value -> ID','value',1,'p_value','update_select_delete.py',161),
  ('value -> literal','value',1,'p_value','update_select_delete.py',162),
  ('literal -> INT','literal',1,'p_literal','update_select_delete.py',165),
  ('literal -> DOUBLE','literal',1,'p_literal','update_select_delete.py',166),
  ('literal -> STRING','literal',1,'p_literal','update_select_delete.py',167),
]
