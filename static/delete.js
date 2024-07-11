$(document).ready(function() {
    $('.delete-news').on('click', function() {
        var newsId = $(this).data('news-id');
        
        $.ajax({
            url: '/delete_news/' + newsId,
            type: 'DELETE',
            success: function(response) {
                alert(response.message); // Выводим сообщение об успешном удалении
                // Дополнительные действия, например, обновление списка новостей на странице
            },
            error: function(error) {
                console.log(error); // В случае ошибки выводим её в консоль
            }
        });
    });
});
