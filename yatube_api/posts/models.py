from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
CHARACTER_LIMIT = 30  # ограничение в количестве символов


class Group(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('ЧПУ', unique=True)
    description = models.TextField('Описание')

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'

    def __str__(self):
        return self.text[:CHARACTER_LIMIT]


class Post(models.Model):
    text = models.TextField(
        'Текст поста',
        help_text='Текст нового поста'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Выберите группу'
    )

    class Meta:
        ordering = ['author']
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

    def __str__(self):
        return self.text[:CHARACTER_LIMIT]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост'
    )
    text = models.TextField('Коментарий')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Коментарии'
        verbose_name = 'Коментарий'

    def __str__(self):
        return self.text[:CHARACTER_LIMIT]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='follower',
        verbose_name='Фолловер'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta():
        verbose_name_plural = 'Подписки'
        verbose_name = 'Подписка'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_employee_user'),
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_prevent_self_follow',
                check=~models.Q(user=models.F('following')),
            ),
        ]

    def __str__(self):
        return f'{self.user} подписался на {self.following}'
