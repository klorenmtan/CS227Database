
# C:\Users\Gladys Tillan\Documents\GitHub\parser\LexerParser\parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '719101FDECF145AEF9E886DE9AD7E415'
    
_lr_action_items = {'DOT':([10,19,38,68,99,],[15,26,55,83,105,]),'EOL':([10,17,19,20,21,24,27,33,34,35,36,37,38,39,45,50,64,65,66,67,71,72,73,75,76,78,82,86,88,91,92,93,100,102,106,108,109,110,],[-39,22,-41,-40,28,42,47,-53,-51,-49,-52,54,-47,-33,-42,69,79,-14,81,-16,-30,-31,-48,-34,-32,-50,-17,-15,-18,-19,-20,-29,-26,-27,-28,-21,-22,-23,]),'ALL':([4,62,],[9,9,]),'INT':([23,31,41,43,44,46,52,53,56,57,58,59,60,88,94,95,96,98,103,108,],[34,34,34,34,34,34,34,34,-36,34,-35,-38,-37,34,34,34,34,34,34,34,]),'SELECT':([0,41,74,95,],[4,62,62,62,]),'ON':([30,51,70,],[49,-24,-25,]),'LPAREN':([23,31,41,43,46,52,53,56,57,58,59,60,88,94,95,96,98,103,108,],[41,41,41,41,41,41,41,-36,74,-35,-38,-37,95,95,95,95,41,41,95,]),'COMMA':([8,10,19,20,21,33,34,36,45,65,89,],[14,-39,-41,-40,14,-53,-51,-52,-42,80,14,]),'WHERE':([10,17,19,20,21,24,27,33,34,35,36,38,45,65,67,73,75,78,82,86,88,89,91,92,93,97,100,102,106,108,109,110,],[-39,23,-41,-40,31,43,46,-53,-51,-49,-52,-47,-42,-14,-16,-48,-34,-50,-17,-15,-18,98,-19,-20,-29,103,-26,-27,-28,-21,-22,-23,]),'JOIN':([10,19,20,21,29,45,51,67,88,89,108,],[-39,-41,-40,32,48,-42,32,32,32,32,32,]),'STRING':([23,31,41,43,44,46,52,53,56,57,58,59,60,88,94,95,96,98,103,108,],[33,33,33,33,33,33,33,33,-36,33,-35,-38,-37,33,33,33,33,33,33,33,]),'NEQ':([33,34,35,36,38,40,73,78,],[-53,-51,-49,-52,-47,56,-48,-50,]),'AND':([33,34,35,36,37,38,39,50,61,64,66,71,72,73,75,76,78,88,94,95,96,104,107,108,],[-53,-51,-49,-52,53,-47,-33,53,53,53,53,53,-31,-48,-34,-32,-50,94,94,94,94,53,53,94,]),'EQ':([25,33,34,35,36,38,40,68,73,78,87,],[44,-53,-51,-49,-52,-47,58,84,-48,-50,90,]),'DOUBLE':([23,31,41,43,44,46,52,53,56,57,58,59,60,88,94,95,96,98,103,108,],[36,36,36,36,36,36,36,36,-36,36,-35,-38,-37,36,36,36,36,36,36,36,]),'NATURAL':([10,19,20,21,45,67,88,89,108,],[-39,-41,-40,29,-42,29,29,29,29,]),'RPAREN':([10,19,20,33,34,35,36,38,39,45,61,63,67,71,72,73,75,76,78,82,88,89,91,92,93,97,100,101,102,104,106,107,108,109,110,],[-39,-41,-40,-53,-51,-49,-52,-47,-33,-42,76,78,-16,-30,-31,-48,-34,-32,-50,-17,-18,-43,-19,-20,-29,-44,-26,106,-27,-45,-28,-46,-21,-22,-23,]),'LT':([33,34,35,36,38,40,73,78,],[-53,-51,-49,-52,-47,59,-48,-50,]),'SET':([13,],[18,]),'ID':([4,6,12,14,15,16,18,23,26,31,32,41,43,46,48,49,52,53,55,56,57,58,59,60,62,80,83,84,85,88,90,94,95,96,98,103,105,108,],[10,13,17,19,20,10,25,38,45,38,51,38,38,38,67,68,38,38,73,-36,38,-35,-38,-37,10,25,87,88,10,38,99,38,38,38,38,38,108,38,]),'$end':([1,2,3,7,22,28,42,47,54,69,79,81,],[-3,-1,0,-2,-10,-6,-4,-7,-11,-8,-5,-9,]),'DELETE':([0,],[5,]),'UPDATE':([0,],[6,]),'OR':([33,34,35,36,37,38,39,50,61,64,66,71,72,73,75,76,78,88,94,95,96,104,107,108,],[-53,-51,-49,-52,52,-47,-33,52,52,52,52,-30,-31,-48,-34,-32,-50,96,96,96,96,52,52,96,]),'FROM':([5,8,9,10,11,19,20,45,77,],[12,-13,-12,-39,16,-41,-40,-42,85,]),'GT':([33,34,35,36,38,40,73,78,],[-53,-51,-49,-52,-47,60,-48,-50,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'literal':([23,31,41,43,44,46,52,53,57,88,94,95,96,98,103,108,],[35,35,35,35,65,35,35,35,35,35,35,35,35,35,35,35,]),'join_list':([21,51,67,88,89,108,],[30,70,30,30,30,30,]),'comp_op':([40,],[57,]),'join_search_condition':([88,94,95,96,108,],[92,100,101,102,110,]),'statement':([0,],[3,]),'update_statement':([0,],[2,]),'delete_statement':([0,],[1,]),'set_clause_list':([18,80,],[24,86,]),'value':([23,31,41,43,46,52,53,57,88,94,95,96,98,103,108,],[40,40,40,40,40,40,40,75,40,40,40,40,40,40,40,]),'comparison_predicate':([23,31,41,43,46,52,53,88,94,95,96,98,103,108,],[39,39,39,39,39,39,39,93,93,93,93,39,39,93,]),'select_columns':([4,62,],[11,77,]),'select_statement':([0,],[7,]),'search_condition':([23,31,41,43,46,52,53,98,103,],[37,50,61,64,66,71,72,104,107,]),'join_clause':([21,67,88,89,108,],[27,82,91,97,109,]),'id_list':([4,16,62,85,],[8,21,8,89,]),'inner_select_statement':([41,74,95,],[63,63,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> update_statement','statement',1,'p_statement','LexerParser.py',107),
  ('statement -> select_statement','statement',1,'p_statement','LexerParser.py',108),
  ('statement -> delete_statement','statement',1,'p_statement','LexerParser.py',109),
  ('update_statement -> UPDATE ID SET set_clause_list EOL','update_statement',5,'p_update_statement','LexerParser.py',114),
  ('update_statement -> UPDATE ID SET set_clause_list WHERE search_condition EOL','update_statement',7,'p_update_statement','LexerParser.py',115),
  ('select_statement -> SELECT select_columns FROM id_list EOL','select_statement',5,'p_select_statement','LexerParser.py',123),
  ('select_statement -> SELECT select_columns FROM id_list join_clause EOL','select_statement',6,'p_select_statement','LexerParser.py',124),
  ('select_statement -> SELECT select_columns FROM id_list WHERE search_condition EOL','select_statement',7,'p_select_statement','LexerParser.py',125),
  ('select_statement -> SELECT select_columns FROM id_list join_clause WHERE search_condition EOL','select_statement',8,'p_select_statement','LexerParser.py',126),
  ('delete_statement -> DELETE FROM ID EOL','delete_statement',4,'p_delete_statement','LexerParser.py',137),
  ('delete_statement -> DELETE FROM ID WHERE search_condition EOL','delete_statement',6,'p_delete_statement','LexerParser.py',138),
  ('select_columns -> ALL','select_columns',1,'p_select_columns','LexerParser.py',146),
  ('select_columns -> id_list','select_columns',1,'p_select_columns','LexerParser.py',147),
  ('set_clause_list -> ID EQ literal','set_clause_list',3,'p_set_clause_list','LexerParser.py',152),
  ('set_clause_list -> ID EQ literal COMMA set_clause_list','set_clause_list',5,'p_set_clause_list','LexerParser.py',153),
  ('join_clause -> NATURAL JOIN ID','join_clause',3,'p_join_clause','LexerParser.py',161),
  ('join_clause -> NATURAL JOIN ID join_clause','join_clause',4,'p_join_clause','LexerParser.py',162),
  ('join_clause -> join_list ON ID EQ ID','join_clause',5,'p_join_clause','LexerParser.py',163),
  ('join_clause -> join_list ON ID EQ ID join_clause','join_clause',6,'p_join_clause','LexerParser.py',164),
  ('join_clause -> join_list ON ID EQ ID join_search_condition','join_clause',6,'p_join_clause','LexerParser.py',165),
  ('join_clause -> join_list ON ID DOT ID EQ ID DOT ID','join_clause',9,'p_join_clause','LexerParser.py',166),
  ('join_clause -> join_list ON ID DOT ID EQ ID DOT ID join_clause','join_clause',10,'p_join_clause','LexerParser.py',167),
  ('join_clause -> join_list ON ID DOT ID EQ ID DOT ID join_search_condition','join_clause',10,'p_join_clause','LexerParser.py',168),
  ('join_list -> JOIN ID','join_list',2,'p_join_list','LexerParser.py',184),
  ('join_list -> JOIN ID join_list','join_list',3,'p_join_list','LexerParser.py',185),
  ('join_search_condition -> AND join_search_condition','join_search_condition',2,'p_join_search_condition','LexerParser.py',193),
  ('join_search_condition -> OR join_search_condition','join_search_condition',2,'p_join_search_condition','LexerParser.py',194),
  ('join_search_condition -> LPAREN join_search_condition RPAREN','join_search_condition',3,'p_join_search_condition','LexerParser.py',195),
  ('join_search_condition -> comparison_predicate','join_search_condition',1,'p_join_search_condition','LexerParser.py',196),
  ('search_condition -> search_condition OR search_condition','search_condition',3,'p_search_condition','LexerParser.py',206),
  ('search_condition -> search_condition AND search_condition','search_condition',3,'p_search_condition','LexerParser.py',207),
  ('search_condition -> LPAREN search_condition RPAREN','search_condition',3,'p_search_condition','LexerParser.py',208),
  ('search_condition -> comparison_predicate','search_condition',1,'p_search_condition','LexerParser.py',209),
  ('comparison_predicate -> value comp_op value','comparison_predicate',3,'p_comparison_predicate','LexerParser.py',217),
  ('comp_op -> EQ','comp_op',1,'p_comp_op','LexerParser.py',222),
  ('comp_op -> NEQ','comp_op',1,'p_comp_op','LexerParser.py',223),
  ('comp_op -> GT','comp_op',1,'p_comp_op','LexerParser.py',224),
  ('comp_op -> LT','comp_op',1,'p_comp_op','LexerParser.py',225),
  ('id_list -> ID','id_list',1,'p_id_list','LexerParser.py',230),
  ('id_list -> ID DOT ID','id_list',3,'p_id_list','LexerParser.py',231),
  ('id_list -> id_list COMMA ID','id_list',3,'p_id_list','LexerParser.py',232),
  ('id_list -> id_list COMMA ID DOT ID','id_list',5,'p_id_list','LexerParser.py',233),
  ('inner_select_statement -> SELECT select_columns FROM id_list','inner_select_statement',4,'p_inner_select_statement','LexerParser.py',246),
  ('inner_select_statement -> SELECT select_columns FROM id_list join_clause','inner_select_statement',5,'p_inner_select_statement','LexerParser.py',247),
  ('inner_select_statement -> SELECT select_columns FROM id_list WHERE search_condition','inner_select_statement',6,'p_inner_select_statement','LexerParser.py',248),
  ('inner_select_statement -> SELECT select_columns FROM id_list join_clause WHERE search_condition','inner_select_statement',7,'p_inner_select_statement','LexerParser.py',249),
  ('value -> ID','value',1,'p_value','LexerParser.py',261),
  ('value -> ID DOT ID','value',3,'p_value','LexerParser.py',262),
  ('value -> literal','value',1,'p_value','LexerParser.py',263),
  ('value -> LPAREN inner_select_statement RPAREN','value',3,'p_value','LexerParser.py',264),
  ('literal -> INT','literal',1,'p_literal','LexerParser.py',272),
  ('literal -> DOUBLE','literal',1,'p_literal','LexerParser.py',273),
  ('literal -> STRING','literal',1,'p_literal','LexerParser.py',274),
]