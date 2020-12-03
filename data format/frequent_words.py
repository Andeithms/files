import json
import xml.etree.ElementTree as ET


def json_file(symbols_number, count_top_words):
    with open('newsafr.json', encoding='UTF-8') as f:
        json_data = json.load(f)
        news_list = []

        for news in json_data['rss']['channel']['items']:
            news_list.append(news['description'])

        string = ' '.join(news_list)
        top_news(string, symbols_number, count_top_words)


def top_news(news, symbols_number, count_top_words):
    filter_words = []
    words_count = {}

    for word in news.split(' '):    # список из слов нужной длины
        if len(word) >= symbols_number:
           filter_words.append(word)

    for word in filter_words:   # словарь с количеством повторений слов
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    counter = 0
    for x in sorted(words_count, key=words_count.get, reverse=True):   # топ 10 самых популярных слов
        print(f'Слово "{x}" с количеством повторений {words_count[x]}')
        counter += 1
        if counter == count_top_words:    # топ самых часто встречаемых слов
            break


def xml_file(symbols_number, count_top_words):
    tree = ET.parse('newsafr.xml')
    root = tree.getroot()
    news_list = []

    for news in root.findall('channel/item'):
        news_list.append(news.find('description').text)

    string = ' '.join(news_list)
    top_news(string, symbols_number, count_top_words)


json_file(6, 10)
print()
xml_file(6, 10)
