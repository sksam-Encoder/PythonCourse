# stoering  5 data  in  DICT  user enter a key then program automatically return the meanings
d2 = {"title": "the heading content of any thing", "abandoned": " leaving a thing after trying every thing ",
      "sticky": "something which stickies any where and became greasy", "express": "express means really fast "
                                                                                   "and best in every thing "
                                                                                   "whatever may it running "
                                                                                   "path or in other",
      "best": "mean very good at every thing which cant be express in any way"}
key = input("enter a word to search meanings")
print(
    d2.get(key, "not Found!!!")
)

