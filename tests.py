from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    def test_add_new_book_add_three_books_in_final_list(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем три книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Ау!')

        assert len(collector.get_books_genre()) == 3

    def test_add_new_book_more_forty_symbols_not_in_final_list(self):

        collector = BooksCollector()
        # добавляем книгу длиной > 40 и проверяем добавилась ли она в список
        collector.add_new_book('Что делать, если ваш кот хочет вас убить, ч.2')

        assert len(collector.get_books_genre()) != 1

    def test_add_new_book_same_name_second_time_not_in_final_list(self):

        collector = BooksCollector()
        #добавляем 2 одинаковые книги и убеждаемся, что принят в список только одно наименование без дубля
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 1

    def test_get_books_genre_in_list(self):
        collector = BooksCollector()
        #проверяем вывод текущего словаря
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Ужасы')
        assert collector.get_books_genre() == {'Колобок': 'Ужасы'}

    def test_set_book_genre_for_book_in_list(self):
        collector = BooksCollector()
        #проверяем способность добавлять жанр к книге из списка и показывать жанр по имени книги
        collector.add_new_book('Хищник')
        collector.set_book_genre('Хищник', 'Ужасы')
        assert collector.get_book_genre('Хищник') == 'Ужасы'

    def test_set_book_genre_without_book_in_list(self):
        collector = BooksCollector()
        #проверяем (не)добавляемость жанра к книге, которой нет в списке
        collector.set_book_genre('Хищник', 'Ужасы')
        assert collector.get_book_genre('Хищник') == None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        #проверяем, выводит ли метод по определенному жанру соответствующую жанру книгу
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        collector.add_new_book('Простоквашино')
        collector.set_book_genre('Простоквашино', 'Мультфильмы')
        collector.add_new_book('Ай! Болит!')
        collector.set_book_genre('Ай! Болит!', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Простоквашино', 'Ай! Болит!']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        #проверяем, выводит ли метод книга, подходящие дл детей по возрастному рейтингу
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        collector.add_new_book('Простоквашино')
        collector.set_book_genre('Простоквашино', 'Мультфильмы')
        collector.add_new_book('Ай! Болит!')
        collector.set_book_genre('Ай! Болит!', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Простоквашино', 'Ай! Болит!']

    def test_add_book_in_favorites_not_in_final_list(self):
        collector = BooksCollector()
        #проверяемя, что нельзя вызвать из списка избранного книгу, которой нет в изначальном списке книг
        collector.add_book_in_favorites('Последний из Могикан')
        assert collector.get_list_of_favorites_books() != ['Последний из Могикан']

    def test_add_book_in_favorites_is_in_final_list(self):
        collector = BooksCollector()
        #проверяем, что можно добавить в избранное книгу и вызвать из избранного
        collector.add_new_book('Чужой')
        collector.add_book_in_favorites('Чужой')
        assert collector.get_list_of_favorites_books() == ['Чужой']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        #проверяем удаляемость книги из избранного списка
        collector.add_new_book('Последний из Могикан')
        collector.add_book_in_favorites('Последний из Могикан')
        collector.delete_book_from_favorites('Последний из Могикан')
        assert collector.get_list_of_favorites_books() == []