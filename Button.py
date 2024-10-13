class Button:

    def __init__(self, num_click=0):
        self.num_click = num_click


    def click(self):
        self.num_click += 1

    def click_count(self):
        print(self.num_click)

    def reset(self):
        self.num_click = 0

but1 = Button(5)
but1.click_count()
but1.click()
but1.click_count()
print('============================')
for i in range(5):
    but1.click()
print('Всего кликов после цикла: ')
but1.click_count()