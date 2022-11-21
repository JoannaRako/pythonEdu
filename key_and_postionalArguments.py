'''
Argumenty kluczowe i pozycyjne
kluczowy - w postaci 'klucz - wartość' (domyślny) (można pominąć)
pozycyjne - liczy się kolejność przy wywołaniu (nie można ich pominąć)
parametry domyślne możemy pominąć

'''

def greet(name, message, separator = ' '):                  # separator => się przypisze do sep z domyślną spacją
    print(message, name, sep = separator)                   # wart (spacja) przypisana jako separator między słowami

greet("Arek", "Hello")                  # Argumenty_pozycyjne

greet(message="Hello", name="Arek")     # Argumenty_kluczowe

greet("Hello", "Arek", "\n")                                # dzięki separator, możemy tu dodać trzecią wart.