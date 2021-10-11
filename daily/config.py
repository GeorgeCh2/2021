COOK_LABEL_LIST = [
    "Cook",
]
MOVIE_LABEL_LIST = [
    "Movie",
]
READ_LABEL_LIST = [
    "Read",
]
DRAMA_LABEL_LIST = [
    "Drama",
]
BANGUMI_LABEL_LIST = [
    "Bangumi",
]
GTD_LABEL_LIST = [
    "GTD",
]
WEEKLY_LABEL_LIST = [
    "Weekly",
]

MY_BLOG_REPO = "GeorgeCh2/blog"
GITHUB_README_COMMENTS = (
    "(<!--START_SECTION:{name}-->\n)(.*)(<!--END_SECTION:{name}-->\n)"
)

# add new label here
LABEL_DICT = {
    "Cook": {"label_list": COOK_LABEL_LIST, "comment_name": "my_cook"},
    "Movie": {"label_list": MOVIE_LABEL_LIST, "comment_name": "my_movie"},
    "Read": {"label_list": READ_LABEL_LIST, "comment_name": "my_read"},
    "Drama": {"label_list": DRAMA_LABEL_LIST, "comment_name": "my_drama"},
    "Bangumi": {"label_list": BANGUMI_LABEL_LIST, "comment_name": "my_bangumi"},
}


##### SHANBAY ######
MY_SHANBAY_USER_NAME = "edwjfe"
SHANBAY_CALENDAR_API = "https://apiv3.shanbay.com/uc/checkin/calendar/dates/?user_id={user_name}&start_date={start_date}&end_date={end_date}"
MY_SHANBAY_URL = f"https://web.shanbay.com/web/users/{MY_SHANBAY_USER_NAME}/zone"


##### BASE COMMENT TABLE ######
BASE_ISSUE_STAT_HEAD = "| Name | Start | Update | \n | ---- | ---- | ---- | \n"
BASE_ISSUE_STAT_TEMPLATE = "| {name} | {start} | {update} | \n"

##### BLOG COMMENT ######
BLOG_ISSUE_STAT_HEAD = (
    "| Name | Start | Update | Comments | \n | ---- | ---- | ---- | ---- |\n"
)
BLOG_ISSUE_STAT_TEMPLATE = "| {name} | {start} | {update} | {comments} | \n"


##### FOOD COMMENT TABLE ######
FOOD_ISSUE_STAT_HEAD = (
    "| Name | First_date | Last_date | Times | \n | ---- | ---- | ---- | ---- |\n"
)
FOOD_ISSUE_STAT_TEMPLATE = "| {name} | {first_date} | {last_date} | {times} |\n"


##### Month Summary ######
MONTH_SUMMARY_HEAD = "| Month | Number | \n | ---- | ---- | \n"

MONTH_SUMMARY_STAT_TEMPLATE = "| {month} | {number} |\n"
