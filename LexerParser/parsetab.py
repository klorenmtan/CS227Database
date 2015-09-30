
# C:\Users\Gladys Tillan\Documents\GitHub\LexerParser\parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '9454019CDF8FD021030A48AE17935EFD'
    
_lr_action_items = {'LPAREN':([24,27,31,37,52,54,55,61,62,63,64,65,87,91,92,93,97,104,108,],[37,37,37,37,37,37,37,-36,-35,79,-37,-38,93,93,93,93,37,37,93,]),'COMMA':([10,11,21,22,23,38,39,43,45,47,89,],[15,-39,-41,-40,15,-53,-52,-51,66,-42,15,]),'DELETE':([0,],[6,]),'ID':([3,5,13,14,15,16,17,24,27,29,31,32,37,48,51,52,54,55,59,60,61,62,63,64,65,66,83,84,86,87,91,92,93,96,97,104,106,108,],[8,11,18,19,21,22,11,40,40,47,40,50,40,68,71,40,40,40,11,78,-36,-35,40,-37,-38,19,87,88,11,40,40,40,40,102,40,40,108,40,]),'LT':([38,39,40,41,42,43,76,78,],[-53,-52,-47,-49,65,-51,-50,-48,]),'OR':([36,38,39,40,41,43,44,46,49,57,72,73,74,75,76,78,80,87,91,92,93,103,107,108,],[55,-53,-52,-47,-49,-51,-33,55,55,55,55,-31,-30,-32,-50,-48,-34,92,92,92,92,55,55,92,]),'EQ':([19,38,39,40,41,42,43,71,76,78,88,],[26,-53,-52,-47,-49,62,-51,83,-50,-48,96,]),'RPAREN':([11,21,22,38,39,40,41,43,44,47,57,58,68,73,74,75,76,78,80,82,87,89,90,94,95,98,99,100,101,103,105,107,108,109,110,],[-39,-41,-40,-53,-52,-47,-49,-51,-33,-42,75,76,-16,-31,-30,-32,-50,-48,-34,-17,-18,-43,-20,-29,-19,-44,-26,-27,105,-45,-28,-46,-21,-23,-22,]),'SET':([8,],[14,]),'$end':([1,2,4,7,25,28,33,53,56,67,69,85,],[-3,-2,-1,0,-10,-4,-6,-7,-11,-5,-8,-9,]),'DOT':([11,21,40,71,102,],[16,29,60,84,106,]),'ALL':([5,59,],[9,9,]),'GT':([38,39,40,41,42,43,76,78,],[-53,-52,-47,-49,64,-51,-50,-48,]),'EOL':([11,18,20,21,22,23,35,36,38,39,40,41,43,44,45,46,47,49,68,72,73,74,75,76,78,80,81,82,87,90,94,95,99,100,105,108,109,110,],[-39,25,28,-41,-40,33,53,56,-53,-52,-47,-49,-51,-33,-14,67,-42,69,-16,85,-31,-30,-32,-50,-48,-34,-15,-17,-18,-20,-29,-19,-26,-27,-28,-21,-23,-22,]),'INT':([24,26,27,31,37,52,54,55,61,62,63,64,65,87,91,92,93,97,104,108,],[43,43,43,43,43,43,43,43,-36,-35,43,-37,-38,43,43,43,43,43,43,43,]),'NATURAL':([11,21,22,23,47,68,87,89,108,],[-39,-41,-40,30,-42,30,30,30,30,]),'NEQ':([38,39,40,41,42,43,76,78,],[-53,-52,-47,-49,61,-51,-50,-48,]),'FROM':([6,9,10,11,12,21,22,47,77,],[13,-12,-13,-39,17,-41,-40,-42,86,]),'WHERE':([11,18,20,21,22,23,35,38,39,40,41,43,45,47,68,76,78,80,81,82,87,89,90,94,95,98,99,100,105,108,109,110,],[-39,24,27,-41,-40,31,52,-53,-52,-47,-49,-51,-14,-42,-16,-50,-48,-34,-15,-17,-18,97,-20,-29,-19,104,-26,-27,-28,-21,-23,-22,]),'JOIN':([11,21,22,23,30,47,50,68,87,89,108,],[-39,-41,-40,32,48,-42,32,32,32,32,32,]),'STRING':([24,26,27,31,37,52,54,55,61,62,63,64,65,87,91,92,93,97,104,108,],[38,38,38,38,38,38,38,38,-36,-35,38,-37,-38,38,38,38,38,38,38,38,]),'SELECT':([0,37,79,93,],[5,59,59,59,]),'DOUBLE':([24,26,27,31,37,52,54,55,61,62,63,64,65,87,91,92,93,97,104,108,],[39,39,39,39,39,39,39,39,-36,-35,39,-37,-38,39,39,39,39,39,39,39,]),'ON':([34,50,70,],[51,-24,-25,]),'UPDATE':([0,],[3,]),'AND':([36,38,39,40,41,43,44,46,49,57,72,73,74,75,76,78,80,87,91,92,93,103,107,108,],[54,-53,-52,-47,-49,-51,-33,54,54,54,54,-31,54,-32,-50,-48,-34,91,91,91,91,54,54,91,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'search_condition':([24,27,31,37,52,54,55,97,104,],[36,46,49,57,72,73,74,103,107,]),'join_search_condition':([87,91,92,93,108,],[90,99,100,101,109,]),'delete_statement':([0,],[1,]),'id_list':([5,17,59,86,],[10,23,10,89,]),'comparison_predicate':([24,27,31,37,52,54,55,87,91,92,93,97,104,108,],[44,44,44,44,44,44,44,94,94,94,94,44,44,94,]),'value':([24,27,31,37,52,54,55,63,87,91,92,93,97,104,108,],[42,42,42,42,42,42,42,80,42,42,42,42,42,42,42,]),'literal':([24,26,27,31,37,52,54,55,63,87,91,92,93,97,104,108,],[41,45,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'set_clause_list':([14,66,],[20,81,]),'select_statement':([0,],[2,]),'update_statement':([0,],[4,]),'join_list':([23,50,68,87,89,108,],[34,70,34,34,34,34,]),'inner_select_statement':([37,79,93,],[58,58,58,]),'select_columns':([5,59,],[12,77,]),'comp_op':([42,],[63,]),'statement':([0,],[7,]),'join_clause':([23,68,87,89,108,],[35,82,95,98,110,]),}

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