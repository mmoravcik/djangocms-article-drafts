from django.test import TestCase

from cms.exceptions import PublicIsUnmodifiable
from cms.signals import post_publish

from djangocms_article_drafts.models import Publishable, PublishPool, publishable_pool
from djangocms_article_drafts.test_project.models import ArticleTest, UnregisteredModel


class GenericPublishingTestCase(TestCase):
    
    def setUp(self):
        publishable_pool.clear()
        Publishable.objects.all().delete()
        publishable_pool.register(ArticleTest.__module__, ArticleTest.__name__)

    def test_pool_clear(self):
        publishable_pool.clear()
        self.assertEquals(publishable_pool.model_pool, {})
    
    def test_register(self):
        publishable_pool_new = PublishPool()
        self.assertEquals(publishable_pool_new.model_pool, {})
        publishable_pool_new.register(ArticleTest.__module__, ArticleTest.__name__)
        self.assertEquals(publishable_pool_new.model_pool, {ArticleTest.__name__: ArticleTest})

    def test_save_signal_creates_new_publishable_instance(self):
        article = ArticleTest()
        article.save()
        self.assertEquals(Publishable.objects.count(), 1)        
        publishable = Publishable.objects.first()
        self.assertEquals(publishable.draft_object_id, article.id)

    def test_publish_signal_flags_as_published(self):
        article = ArticleTest()
        article.save()
        post_publish.send(ArticleTest, instance=article)
        publishable = Publishable.objects.get(draft_object_id=article.id)
        self.assertFalse(publishable.is_draft)
        
    def test_publish_signal_assigned_published_object_id(self):
        article = ArticleTest()
        article.save()
        post_publish.send(ArticleTest, instance=article)
        publishable = Publishable.objects.get(draft_object_id=article.id)
        published_article = ArticleTest.objects.last()
        self.assertEquals(publishable.published_object_id, published_article.id)

    def test_exception_if_article_is_published(self):
        article = ArticleTest()
        article.save()
        post_publish.send(ArticleTest, instance=article)
        
        with self.assertRaises(PublicIsUnmodifiable):
            post_publish.send(ArticleTest, instance=article)

    def test_cannot_publish_unregistered_model_class(self):
        unregistered_model = UnregisteredModel()
        post_publish.send(UnregisteredModel, instance=unregistered_model)

        self.assertEquals(Publishable.objects.count(), 0)
