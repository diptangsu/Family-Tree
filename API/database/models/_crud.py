from database import db

class CRUDMixin:
    @classmethod
    def get(cls, pk):
        return cls.query.get(pk)

    @classmethod
    def get_by(cls, **kwargs):
        user = cls.query.filter_by(**kwargs).first()
        return user

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            self.save()
        return self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except Exception:
                db.session.rollback()
                raise
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()
