
# C:\Users\Gladys Tillan\Desktop\227\data\parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = 'EA1A6EF3953818F96B3BF2EF3F1F6A01'
    
_lr_action_items = {'EQ':([20,25,26,28,30,31,32,65,66,81,88,],[34,-49,43,-45,-47,-50,-51,-46,-48,83,97,]),'INT':([19,29,34,36,39,43,44,45,46,47,53,54,58,86,87,89,92,94,95,105,],[25,25,25,25,25,-33,-35,25,-36,-34,25,25,25,25,25,25,25,25,25,25,]),'LT':([25,26,28,30,31,32,65,66,],[-49,46,-45,-47,-50,-51,-46,-48,]),'EOL':([14,21,23,24,25,27,28,30,31,32,33,37,55,56,59,62,63,65,66,67,69,70,73,75,78,80,87,91,93,96,99,101,103,105,106,107,],[18,35,-37,38,-49,-31,-45,-47,-50,-51,52,57,-14,72,74,-38,-32,-46,-48,-30,-28,-29,79,-16,-15,-17,-18,-19,-27,-20,-25,-24,-26,-21,-23,-22,]),'DELETE':([0,],[3,]),'UPDATE':([0,],[4,]),'WHERE':([14,21,23,24,25,28,30,31,32,37,55,62,63,65,66,75,78,80,82,85,87,91,93,96,99,101,103,105,106,107,],[19,36,-37,39,-49,-45,-47,-50,-51,58,-14,-38,-32,-46,-48,-16,-15,-17,86,89,-18,-19,-27,-20,-25,-24,-26,-21,-23,-22,]),'SET':([9,],[15,]),'ALL':([5,51,],[13,13,]),'DOT':([28,81,102,],[48,84,104,]),'GT':([25,26,28,30,31,32,65,66,],[-49,44,-45,-47,-50,-51,-46,-48,]),'COMMA':([10,11,22,23,24,25,31,32,55,62,82,],[16,-39,-40,-37,42,-49,-50,-51,71,-38,42,]),'AND':([25,27,28,30,31,32,33,50,56,59,63,65,66,67,69,70,73,87,90,92,94,95,98,105,],[-49,-31,-45,-47,-50,-51,54,54,54,54,-32,-46,-48,-30,54,-29,54,95,54,95,95,95,54,95,]),'STRING':([19,29,34,36,39,43,44,45,46,47,53,54,58,86,87,89,92,94,95,105,],[32,32,32,32,32,-33,-35,32,-36,-34,32,32,32,32,32,32,32,32,32,32,]),'OR':([25,27,28,30,31,32,33,50,56,59,63,65,66,67,69,70,73,87,90,92,94,95,98,105,],[-49,-31,-45,-47,-50,-51,53,53,53,53,-32,-46,-48,-30,-28,-29,53,92,53,92,92,92,53,92,]),'RPAREN':([23,25,27,28,30,31,32,49,50,62,63,65,66,67,69,70,75,80,82,85,87,90,91,93,96,98,99,100,101,103,105,106,107,],[-37,-49,-31,-45,-47,-50,-51,66,67,-38,-32,-46,-48,-30,-28,-29,-16,-17,-41,-42,-18,-43,-19,-27,-20,-44,-25,103,-24,-26,-21,-23,-22,]),'DOUBLE':([19,29,34,36,39,43,44,45,46,47,53,54,58,86,87,89,92,94,95,105,],[31,31,31,31,31,-33,-35,31,-36,-34,31,31,31,31,31,31,31,31,31,31,]),'NATURAL':([23,24,62,75,82,87,105,],[-37,40,-38,40,40,40,40,]),'ID':([4,5,8,15,16,17,19,29,36,39,41,42,43,44,45,46,47,48,51,53,54,58,60,71,76,77,83,84,86,87,89,92,94,95,97,104,105,],[9,11,14,20,22,23,28,28,28,28,61,62,-33,-35,28,-36,-34,65,11,28,28,28,75,20,81,23,87,88,28,28,28,28,28,28,102,105,28,]),'SELECT':([0,29,64,94,],[5,51,51,51,]),'JOIN':([23,24,40,62,75,82,87,105,],[-37,41,60,-38,41,41,41,41,]),'LPAREN':([19,29,36,39,43,44,45,46,47,53,54,58,86,87,89,92,94,95,105,],[29,29,29,29,-33,-35,64,-36,-34,29,29,29,29,94,29,94,94,94,94,]),'NEQ':([25,26,28,30,31,32,65,66,],[-49,47,-45,-47,-50,-51,-46,-48,]),'FROM':([3,10,11,12,13,22,68,],[8,-13,-39,17,-12,-40,77,]),'$end':([1,2,6,7,18,35,38,52,57,72,74,79,],[0,-3,-1,-2,-10,-4,-6,-11,-7,-5,-8,-9,]),'ON':([61,],[76,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'join_search_condition':([87,92,94,95,105,],[96,99,100,101,106,]),'value':([19,29,36,39,45,53,54,58,86,87,89,92,94,95,105,],[26,26,26,26,63,26,26,26,26,26,26,26,26,26,26,]),'statement':([0,],[1,]),'set_clause_list':([15,71,],[21,78,]),'comparison_predicate':([19,29,36,39,53,54,58,86,87,89,92,94,95,105,],[27,27,27,27,27,27,27,27,93,27,93,93,93,93,]),'table_list':([17,77,],[24,82,]),'select_statement':([0,],[7,]),'inner_select_statement':([29,64,94,],[49,49,49,]),'search_condition':([19,29,36,39,53,54,58,86,89,],[33,50,56,59,69,70,73,90,98,]),'select_columns':([5,51,],[12,68,]),'literal':([19,29,34,36,39,45,53,54,58,86,87,89,92,94,95,105,],[30,30,55,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'delete_statement':([0,],[2,]),'comp_op':([26,],[45,]),'join_clause':([24,75,82,87,105,],[37,80,85,91,107,]),'update_statement':([0,],[6,]),'column_list':([5,51,],[10,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> update_statement','statement',1,'p_statement','LexerParser.py',112),
  ('statement -> select_statement','statement',1,'p_statement','LexerParser.py',113),
  ('statement -> delete_statement','statement',1,'p_statement','LexerParser.py',114),
  ('update_statement -> UPDATE ID SET set_clause_list EOL','update_statement',5,'p_update_statement','LexerParser.py',119),
  ('update_statement -> UPDATE ID SET set_clause_list WHERE search_condition EOL','update_statement',7,'p_update_statement','LexerParser.py',120),
  ('select_statement -> SELECT select_columns FROM table_list EOL','select_statement',5,'p_select_statement','LexerParser.py',128),
  ('select_statement -> SELECT select_columns FROM table_list join_clause EOL','select_statement',6,'p_select_statement','LexerParser.py',129),
  ('select_statement -> SELECT select_columns FROM table_list WHERE search_condition EOL','select_statement',7,'p_select_statement','LexerParser.py',130),
  ('select_statement -> SELECT select_columns FROM table_list join_clause WHERE search_condition EOL','select_statement',8,'p_select_statement','LexerParser.py',131),
  ('delete_statement -> DELETE FROM ID EOL','delete_statement',4,'p_delete_statement','LexerParser.py',143),
  ('delete_statement -> DELETE FROM ID WHERE search_condition EOL','delete_statement',6,'p_delete_statement','LexerParser.py',144),
  ('select_columns -> ALL','select_columns',1,'p_select_columns','LexerParser.py',152),
  ('select_columns -> column_list','select_columns',1,'p_select_columns','LexerParser.py',153),
  ('set_clause_list -> ID EQ literal','set_clause_list',3,'p_set_clause_list','LexerParser.py',158),
  ('set_clause_list -> ID EQ literal COMMA set_clause_list','set_clause_list',5,'p_set_clause_list','LexerParser.py',159),
  ('join_clause -> NATURAL JOIN ID','join_clause',3,'p_join_clause','LexerParser.py',167),
  ('join_clause -> NATURAL JOIN ID join_clause','join_clause',4,'p_join_clause','LexerParser.py',168),
  ('join_clause -> JOIN ID ON ID EQ ID','join_clause',6,'p_join_clause','LexerParser.py',169),
  ('join_clause -> JOIN ID ON ID EQ ID join_clause','join_clause',7,'p_join_clause','LexerParser.py',170),
  ('join_clause -> JOIN ID ON ID EQ ID join_search_condition','join_clause',7,'p_join_clause','LexerParser.py',171),
  ('join_clause -> JOIN ID ON ID DOT ID EQ ID DOT ID','join_clause',10,'p_join_clause','LexerParser.py',172),
  ('join_clause -> JOIN ID ON ID DOT ID EQ ID DOT ID join_clause','join_clause',11,'p_join_clause','LexerParser.py',173),
  ('join_clause -> JOIN ID ON ID DOT ID EQ ID DOT ID join_search_condition','join_clause',11,'p_join_clause','LexerParser.py',174),
  ('join_search_condition -> AND join_search_condition','join_search_condition',2,'p_join_search_condition','LexerParser.py',190),
  ('join_search_condition -> OR join_search_condition','join_search_condition',2,'p_join_search_condition','LexerParser.py',191),
  ('join_search_condition -> LPAREN join_search_condition RPAREN','join_search_condition',3,'p_join_search_condition','LexerParser.py',192),
  ('join_search_condition -> comparison_predicate','join_search_condition',1,'p_join_search_condition','LexerParser.py',193),
  ('search_condition -> search_condition OR search_condition','search_condition',3,'p_search_condition','LexerParser.py',203),
  ('search_condition -> search_condition AND search_condition','search_condition',3,'p_search_condition','LexerParser.py',204),
  ('search_condition -> LPAREN search_condition RPAREN','search_condition',3,'p_search_condition','LexerParser.py',205),
  ('search_condition -> comparison_predicate','search_condition',1,'p_search_condition','LexerParser.py',206),
  ('comparison_predicate -> value comp_op value','comparison_predicate',3,'p_comparison_predicate','LexerParser.py',217),
  ('comp_op -> EQ','comp_op',1,'p_comp_op','LexerParser.py',222),
  ('comp_op -> NEQ','comp_op',1,'p_comp_op','LexerParser.py',223),
  ('comp_op -> GT','comp_op',1,'p_comp_op','LexerParser.py',224),
  ('comp_op -> LT','comp_op',1,'p_comp_op','LexerParser.py',225),
  ('table_list -> ID','table_list',1,'p_table_list','LexerParser.py',230),
  ('table_list -> table_list COMMA ID','table_list',3,'p_table_list','LexerParser.py',231),
  ('column_list -> ID','column_list',1,'p_column_list','LexerParser.py',239),
  ('column_list -> column_list COMMA ID','column_list',3,'p_column_list','LexerParser.py',240),
  ('inner_select_statement -> SELECT select_columns FROM table_list','inner_select_statement',4,'p_inner_select_statement','LexerParser.py',248),
  ('inner_select_statement -> SELECT select_columns FROM table_list join_clause','inner_select_statement',5,'p_inner_select_statement','LexerParser.py',249),
  ('inner_select_statement -> SELECT select_columns FROM table_list WHERE search_condition','inner_select_statement',6,'p_inner_select_statement','LexerParser.py',250),
  ('inner_select_statement -> SELECT select_columns FROM table_list join_clause WHERE search_condition','inner_select_statement',7,'p_inner_select_statement','LexerParser.py',251),
  ('value -> ID','value',1,'p_value','LexerParser.py',263),
  ('value -> ID DOT ID','value',3,'p_value','LexerParser.py',264),
  ('value -> literal','value',1,'p_value','LexerParser.py',265),
  ('value -> LPAREN inner_select_statement RPAREN','value',3,'p_value','LexerParser.py',266),
  ('literal -> INT','literal',1,'p_literal','LexerParser.py',277),
  ('literal -> DOUBLE','literal',1,'p_literal','LexerParser.py',278),
  ('literal -> STRING','literal',1,'p_literal','LexerParser.py',279),
]