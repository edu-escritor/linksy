from api.models import Page, User
from api.validators.validate_ownership import ValidateOwnership
from api.validators.validate_page_can_be_deleted import ValidatePageCanBeDeleted
from api.validators.validate_page_title_exists import ValidatePageTitleExists


# noinspection PyMethodMayBeStatic
class PageHandler:

    def retrieve(self, user: User, page: Page) -> Page:
        ValidateOwnership.validate(user, page)
        return page

    def list(self, user: User):
        return Page.objects.filter(user=user)

    def create(self, user: User, data: dict) -> Page:
        ValidatePageTitleExists.validate(
            title=data["title"],
            user=user,
        )

        return Page.objects.create(
            user=user,
            **data,
        )

    def update(self, user: User, page: Page, data: dict) -> Page:
        ValidateOwnership.validate(user, page)

        if "title" in data:
            ValidatePageTitleExists.validate(
                title=data["title"],
                user=user,
                page=page,
            )

        for field, value in data.items():
            setattr(page, field, value)

        page.save()

        return page

    def delete(self, user: User, page: Page) -> None:
        ValidateOwnership.validate(user, page)
        ValidatePageCanBeDeleted.validate(page)
        page.delete()
