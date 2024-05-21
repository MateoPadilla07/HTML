program CelciusF;

var
  celsius, fahrenheit: real;

begin
  writeln('Ingrese la temperatura en grados Celsius');
  readln(celsius);

  fahrenheit := (celsius * 9/5) + 32;

  writeln ('La temperatura en grados fahrenheit es: ', fahrenheit:0:2);

end.