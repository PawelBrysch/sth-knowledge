************************************
_SELECT
************************************
basic												SELECT * 
													FROM <_table, i.e. people>
													WHERE <_statement, i.e. age>18 >
													ORDER BY <_value, i.e. salary> ASC

basic join (niewlasciwy)							SELECT k.imie, k.nazwisko, zamowienia.data
													FROM klienci AS k, zamowienia 
													WHERE klienci.idklienta=zamowienia.idklienta
								
* przedzial											WHERE <_value> BETWEEN _lower and _upper
* "regexy" ->										WHERE some_string like "Beginning%"
* subquery - dwa resultaty ->						1) tablica, 2) wartosc (gdy agregat)
* czy mozna mieszac aliasy i oryginal? ->			NIE										

							
************************************
_UPDATE 
************************************
basic usage->										UPDATE _table 
													SET _field="new value" 
													WHERE ...	


************************************
_INSERT 
************************************
basic->												INSERT INTO _table
													VALUES 
														(NULL, "val1", "val2", "val3")
			
* NULL?-> 											autoinkrementacja
** jaki jest tego plus?-> 							mozna wstawic NIEPELNE rekordy
												
*change _order										INSERT INTO _table
													(field2, field1, field3, id) 
													VALUES 
														("val2", "val1", "val3", NULL)
													

*many records										INSERT INTO _table
													VALUES
													(record1),
													(record2)
		
		
************************************
_DELETE/_TRUNCATE/_DROP
************************************	
usuwanie rekordu									DELETE FROM <_table>
													WHERE <_statement>
												
usuniecie rekordow z tabeli							TRUNCATE TABLE <_table>
usuniecie tabeli									DROP TABLE <_table>
if _exists\											DROP TABLE nazwa_tabeli IF EXISTS




		
		
		
		
		
		
		
		
		
		
		