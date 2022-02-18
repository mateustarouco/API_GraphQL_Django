import graphene
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredient, Teste

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = "__all__"

class TesteType(DjangoObjectType):
    class Meta:
        model = Teste
        fields = "__all__"

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    teste = graphene.List(TesteType)
    teste_by_id = graphene.Field(TesteType, id=graphene.String())

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None  

    def resolve_teste(root, info, **kwargs):
        # Querying a list
        return Teste.objects.all()

    def resolve_teste_by_id(root, info, id):
        # Querying a single question
        return Teste.objects.get(pk=id)
        


schema = graphene.Schema(query=Query)