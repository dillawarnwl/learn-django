from django.core.management.base import BaseCommand, CommandError
from base.models import Category

class Command(BaseCommand):
    help = "To manage custom commands"

    def add_arguments(self, parser):
        parser.add_argument(
            '--add',
            dest='add_argument',
            type=str,
            nargs='?',
            help='Specify the category name to add'
        )
        parser.add_argument(
            '--delete',
            dest='delete_argument',
            type=str,
            nargs='?',
            help='Specify the category name to delete'
        )
        parser.add_argument(
            '--update',
            dest='update_argument',
            type=str,
            nargs=2,
            metavar=('old_name', 'new_name'),
            help='Specify the old and new category names to update'
        )
        parser.add_argument(
            '--read',
            action='store_true',
            help='Read all categories'
        )

    def handle(self, *args, **options):
        try:
            add_argument = options['add_argument']
            delete_argument = options['delete_argument']
            update_arguments = options['update_argument']
            read_all = options['read']

            if add_argument:
                existing_categories = Category.objects.filter(name=add_argument)

                if existing_categories.exists():
                    print(f"{add_argument} already exists.")
                else:
                    Category.objects.create(name=add_argument)
                    print(f"{add_argument} added successfully!")

            if delete_argument:
                categories_to_delete = Category.objects.filter(name=delete_argument)

                if categories_to_delete.exists():
                    categories_to_delete.delete()
                    print(f'{delete_argument} deleted successfully!')
                else:
                    print(f'No category found with the name {delete_argument}.')

            if update_arguments:
                old_name, new_name = update_arguments
                category_to_update = Category.objects.filter(name=old_name).first()

                if category_to_update:
                    category_to_update.name = new_name
                    category_to_update.save()
                    print(f'{old_name} updated to {new_name} successfully!')
                else:
                    print(f'No category found with the name {old_name}.')

            if read_all:
                all_categories = Category.objects.all()

                if all_categories.exists():
                    print("All Categories:")
                    for category in all_categories:
                        print(f'- {category.name}')
                else:
                    print("No categories found.")

        except Exception as e:
            raise CommandError(e)
