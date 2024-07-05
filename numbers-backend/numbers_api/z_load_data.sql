INSERT INTO numbers_dashboard_numberm (name, description, url_end_point, enable, min_len, is_serie) 
VALUES 
('Correlativos', 
'Son números naturales consecutivos que se obtienen incrementando en una unidad al número inmediato anterior.', 
'numbers/correlativos/', true, 1, false),

('Pares', 
'Los números pares son aquellos números enteros divisibles por 2.', 
'numbers/pares/', true, 1, false),

('Primos', 
'Los números primos son los números naturales que tienen únicamente dos divisores: 1 y si mísmo.', 
'numbers/primos/', true, 1, false),

('Felices', 
'Los números felices se obtienen al sumar el cuadrado de cada uno de sus dígitos, y repetir la operación con el resultado obtenido las veces necesarias hasta que dicha suma de 1 (siendo el número felíz) o hasta que se obtenga un resultado ya obtenido (ingresando de este modo a un loop infinito, resultando el número no felíz).', 
'numbers/felices/', true, 1, false),

('Impares', 
'Los números impares son aquellos números enteros que no son divisibles por 2.', 
'numbers/impares/', true, 1 , false),

('Serie de Fibonacci', 
'Es una serie infinita de números naturales cuyos primeros dos elementos son 0 y 1, y los restantes se obtienen sumando los dos elementos inmediatos anteriores.', 
'numbers/fibonacci/', true, 2 , true),

('Sucesión de Lucas', 
'Los números de Lucas, son una sucesión infinita de números naturales, cuyos primeros dos elementos son 2 y 1, y los restantes se obtienen sumando los dos elementos inmediatos anteriores.', 
'numbers/lucas/', true, 2 , true),

('Sucesión de Pell', 
'Los números de Pell, son una sucesión infinita de números naturales, cuyos primeros dos elementos son 0 y 1, y los restantes se obtienen sumando el doble del último elemento al penúltimo elemento.', 
'numbers/pell/', true, 2 , true),

('Sucesión de Jacobsthal', 
'Los números de Jacobsthal, son una sucesión infinita de números naturales, cuyos primeros dos elementos son 0 y 1, y los restantes se obtienen sumando el último elemento al doble del penúltimo elemento.', 
'numbers/jacobsthal/', true, 2 , true);


DELETE FROM numbers_dashboard_numberm;
