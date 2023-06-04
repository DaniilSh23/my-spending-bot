from pyrogram.types import InlineKeyboardButton, WebAppInfo

from settings.config import BASE_HOST_URL, STATISTIC_LINK, SUBSCRIPTION_LINK, SUPPORT_LINK

BUTTONS_DCT = {
    'ADMIN_PANEL': InlineKeyboardButton(
        text=f'⌨️Админ-панель',
        url=f'{BASE_HOST_URL}admin/'
    ),

    # Главное меню
    'MY_ACCS': InlineKeyboardButton(
        text=f'🗂 Мои аккаунты',
        callback_data='my_accs'
    ),
    'MY_CHANNELS': InlineKeyboardButton(
        text=f'📢 Мои каналы',
        callback_data='my_chnls'
    ),
    'STATISTIC': InlineKeyboardButton(  # TODO: кнопку потом удалить
        text=f'📊 Статистика',
        web_app=WebAppInfo(url=STATISTIC_LINK)
    ),
    'SUBSCRIPTION': InlineKeyboardButton(   # TODO: кнопку потом удалить
        text=f'🗞 Подписка',
        web_app=WebAppInfo(url=SUBSCRIPTION_LINK)
    ),
    'SUPPORT': InlineKeyboardButton(
        text=f'🛟 Поддержка',
        web_app=WebAppInfo(url=SUPPORT_LINK)
    ),
    'INSTRUCTION': InlineKeyboardButton(
        text=f'👩🏼‍🏫 Инструкция',
        callback_data='instruction'
    ),

    # Ниже старые кнопки
    'TRANSACTIONS_STORY': InlineKeyboardButton(
        text=f'🧾ИСТОРИЯ ОПЕРАЦИЙ',
        callback_data='transactions_story'
    ),
    'CANCEL_AND_CLEAR_STATE': InlineKeyboardButton(
        text=f'❌Отменить',
        callback_data='cancel_and_clear_state'
    ),
    'BACK_TO_HEAD_PAGE': InlineKeyboardButton(
        text=f'🔙На главную',
        callback_data='back_to_head_page'
    ),

    # Выбор кол-ва редиректов
    'MINUS_REDIRECT': InlineKeyboardButton(
        text=f'➖',
        callback_data='minus_redirect 1'
    ),
    'PLUS_REDIRECT': InlineKeyboardButton(
        text=f'➕',
        callback_data='plus_redirect 1'
    ),
    'MINUS_10_REDIRECT': InlineKeyboardButton(
        text=f'➖10',
        callback_data='minus_redirect 10'
    ),
    'PLUS_10_REDIRECT': InlineKeyboardButton(
        text=f'➕10',
        callback_data='plus_redirect 10'
    ),
    'MINUS_100_REDIRECT': InlineKeyboardButton(
        text=f'➖100',
        callback_data='minus_redirect 100'
    ),
    'PLUS_100_REDIRECT': InlineKeyboardButton(
        text=f'➕100',
        callback_data='plus_redirect 100'
    ),
    'MINUS_1000_REDIRECT': InlineKeyboardButton(
        text=f'➖1000',
        callback_data='minus_redirect 1000'
    ),
    'PLUS_1000_REDIRECT': InlineKeyboardButton(
        text=f'➕1000',
        callback_data='plus_redirect 1000'
    ),
    'TO_LINK_SHORTENING': InlineKeyboardButton(
        text=f'След.шаг➡️',
        callback_data='to_link_shortening'
    ),

    # Выбор сервисов для сокращения ссылок
    'cutt.ly': InlineKeyboardButton(
        text=f'🔹cutt.ly',
        callback_data='short_link cutt.ly'
    ),
    'cutt.us': InlineKeyboardButton(
        text=f'🔹cutt.us',
        callback_data='short_link cutt.us'
    ),
    'clck.ru': InlineKeyboardButton(
        text=f'🔹clck.ru',
        callback_data='short_link clck.ru'
    ),
    'kortlink.dk': InlineKeyboardButton(
        text=f'🔹kortlink.dk',
        callback_data='short_link kortlink.dk'
    ),
    'gg.gg': InlineKeyboardButton(
        text=f'🔹gg.gg',
        callback_data='short_link gg.gg'
    ),
    't9y.me': InlineKeyboardButton(
        text=f'🔹t9y.me',
        callback_data='short_link t9y.me'
    ),
    'custom_domain': InlineKeyboardButton(
        text=f'🔹Наши домены ⚜️',
        callback_data='short_link custom_domain'
    ),

    # Кнопка для раздела статистики
    'CHECK_MORE': InlineKeyboardButton(
        text='🔂Проверить ещё',
        callback_data='get_statistic'
    ),

    # Раздел платежей
    'QIWI_PAY_METHD': InlineKeyboardButton(
        text='🪙QIWI',
        callback_data='pay_method qiwi',
    ),
    'CRYSTAL_PAY_METHD': InlineKeyboardButton(
        text='🌑 Crystal Pay',
        callback_data='pay_method crystal',
    ),
    'TO_CARD_PAY_METHD': InlineKeyboardButton(
        text='🌕 Перевод на карту',
        callback_data='pay_to_card',
    ),
    'CONFIRM_PAYMENT': InlineKeyboardButton(
        text='✅Подтвердить оплату',
        callback_data='confirm_payment',
    ),
    'CANCEL_PAYMENT': InlineKeyboardButton(
        text='❌Отменить оплату',
        callback_data='cancel_payment',
    ),
    'I_PAYD_TO_CARD': InlineKeyboardButton(
        text='✅Я перевёл',
        callback_data='i_payd_to_card',
    ),
}
