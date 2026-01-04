import sys
class UpperPrint:

    def __enter__(self):  
        self.standard_output = sys.stdout.write
        def sss(text):
            return self.standard_output(text.upper()) 
        sys.stdout.write = sss
    def __exit__(self, *exc_info):
        sys.stdout.write = self.standard_output 
        

print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with UpperPrint():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')