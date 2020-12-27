import views

routes = {
    '/': views.main_view,
    '/create-course/': views.create_course,
    '/course-list/': views.course_list,
    '/create-category/': views.create_category,
    # '/about/': views.about_view,
    # '/contact/': views.contact_view,
    # '/other/': views.Other(),
}