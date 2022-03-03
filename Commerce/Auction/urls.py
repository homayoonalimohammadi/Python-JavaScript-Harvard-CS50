from django.urls import path, re_path
from .views import (
    index_view,
    listing_view,
    create_listing_view,
    edit_listing_view,
    delete_listing_view,
    close_listing_view,
    login_view,
    logout_view,
    register_view,
    search_view,
    toggle_watch,
    watchlist_view,
    add_comment_view,
    delete_comment_view,
    category_view,
    category_list_view,
    add_bid_view,
    active_index_view,
    my_listings_view,
)


app_name = 'auction'
urlpatterns = [
    path('', index_view, name='index'),
    path('active/', active_index_view, name='active_index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('listings/search/', search_view, name='search'),
    path('listings/create/', create_listing_view, name='create_listing'),
    path('listings/watchlist/', watchlist_view, name='watchlist'),
    path('listings/my_listings/', my_listings_view, name='my_listings'),
    path('listings/category/', category_list_view, name='category_list'),
    path('listings/category/<int:id>/', category_view, name='category'),
    path('listings/<int:id>/', listing_view ,name='listing'),
    path('listings/<int:id>/bid', add_bid_view, name='add_bid'),
    path('listings/<int:id>/edit/', edit_listing_view, name='edit_listing'),
    path('listings/<int:id>/delete/', delete_listing_view, name='delete_listing'),
    path('listings/<int:id>/close/', close_listing_view, name='close_listing'),
    path('listings/<int:id>/toggle-watch/', toggle_watch, name='toggle_watch'),
    path('listings/<int:id>/comment/', add_comment_view, name='comment'),
    path('listings/<int:id>/comment/delete/<int:comment_id>/', delete_comment_view, name='delete_comment'),
]