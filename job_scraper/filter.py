

def get_words_for_filter():
    pass

def get_IDs_of_offers_to_filter():
    pass

def get_name_of_offer(id):
    pass

def is_rejected(name, words_for_filter):
    pass

def update_offer_after_filtering(id, is_rejected):
    pass

def reject_offers_by_name():
    words_for_filter = get_words_for_filter()
    IDs_of_offers_to_filter = get_IDs_of_offers_to_filter()

    for id in IDs_of_offers_to_filter():
        name = get_name_of_offer(id)
        is_offer_rejected = is_rejected(name, words_for_filter)
        update_offer_after_filtering(id, is_offer_rejected)



if __name__ == '__main__':
    a=1