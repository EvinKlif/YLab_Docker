from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from database import get_db
from src import models
from src.schemas import Menu, Submenu, Dishes

router = APIRouter(tags=['Api'])

# Get all menu


@router.get('/api/v1/menus')
def get_all_menu(db: Session = Depends(get_db)):
    return db.query(models.Menu).all()


# Get one menu


@router.get('/api/v1/menus/{menu_id}')
def get_one_menu(menu_id: str, db: Session = Depends(get_db)):
    items = db.query(models.Menu).filter(models.Menu.target_menus_id == menu_id).first()
    submenus_count = len(db.query(models.Submenu).all())
    dishes_count = len(db.query(models.Dishes).all())
    if not items:
        raise HTTPException(status_code=404, detail='menu not found')
    return {'id': items.target_menus_id, 'title': items.target_menus_title,\
            "description": items.target_menus_description, "submenus_count": submenus_count,\
            'dishes_count': dishes_count}


# Create menu

@router.post('/api/v1/menus', status_code=status.HTTP_201_CREATED)
def create_menu(item: Menu, db: Session = Depends(get_db)):
    menu_model = models.Menu()
    menu_model.target_menus_id = item.id
    menu_model.target_menus_title = item.title
    menu_model.target_menus_description = item.description
    db.add(menu_model)
    db.commit()
    db.refresh(menu_model)
    return item


# Update menu

@router.patch('/api/v1/menus/{menu_id}')
def update_menu(menu_id: str, item: Menu, db: Session = Depends(get_db)):
    menu_model = db.query(models.Menu).filter(models.Menu.target_menus_id == menu_id).first()
    menu_model.target_menus_title = item.title
    menu_model.target_menus_description = item.description
    db.add(menu_model)
    db.commit()
    db.refresh(menu_model)
    return item


# Remove menu

@router.delete('/api/v1/menus/{menu_id}')
def delete_menu(menu_id: str, db: Session = Depends(get_db)):
    db.query(models.Menu).filter(models.Menu.target_menus_id == menu_id).delete()
    db.commit()
    return "Success"


# Get all submenu

@router.get('/api/v1/menus/{menu_id}/submenus')
def get_all_menus(db: Session = Depends(get_db)):
    return db.query(models.Submenu).all()


# Create submenu

@router.post('/api/v1/menus/{menu_id}/submenus', status_code=status.HTTP_201_CREATED)
def create_submenu(menu_id: str, item: Submenu, db: Session = Depends(get_db)):
    submenu_model = models.Submenu()
    submenu_model.target_submenus_id = item.id
    submenu_model.target_submenus_title = item.title
    submenu_model.target_submenus_description = item.description
    db.add(submenu_model)
    db.commit()
    db.refresh(submenu_model)
    return item


# Get one submenu

@router.get('/api/v1/menus/{menu_id}/submenus/{sud_id}')
def get_one_submenu(sud_id: str, db: Session = Depends(get_db)):
    sub = db.query(models.Submenu).filter(models.Submenu.target_submenus_id == sud_id).first()
    dishes_count = len(db.query(models.Dishes).all())
    if not sub:
        raise HTTPException(status_code=404, detail='submenu not found')
    return {'id': sub.target_submenus_id, 'title': sub.target_submenus_title,\
            "description": sub.target_submenus_description, "dishes_count": dishes_count}


# Update submenu

@router.patch('/api/v1/menus/{menu_id}/submenus/{sub_id}')
def update_submenu(sub_id: str, item: Submenu, db: Session = Depends(get_db)):
    sub_model = db.query(models.Submenu).filter(models.Submenu.target_submenus_id == sub_id).first()
    sub_model.target_submenus_title = item.title
    sub_model.target_submenus_description = item.description
    db.add(sub_model)
    db.commit()
    db.refresh(sub_model)
    return item


# Delete menu

@router.delete('/api/v1/menus/{menu_id}/submenus/{sub_id}')
def delete_submenu(sub_id: str, db: Session = Depends(get_db)):
    db.query(models.Submenu).filter(models.Submenu.target_submenus_id == sub_id).delete()
    db.commit()
    return "Success"


# Get all dishes

@router.get('/api/v1/menus/{menu_id}/submenus/{sub_id}/dishes')
def get_all_dishes(db: Session = Depends(get_db)):
    return db.query(models.Dishes).all()


# Create dishes

@router.post('/api/v1/menus/{menu_id}/submenus/{sub_id}/dishes', status_code=status.HTTP_201_CREATED)
def create_dishes(sub_id: str,item: Dishes, db: Session = Depends(get_db)):
    dishes_model = models.Dishes()
    dishes_model.target_dishes_id = item.id
    dishes_model.target_dishes_title = item.title
    dishes_model.target_dishes_description = item.description
    dishes_model.target_dishes_price = item.price
    dishes_model.submenus_id = sub_id
    db.add(dishes_model)
    db.commit()
    db.refresh(dishes_model)
    return item


# Get one dishes

@router.get('/api/v1/menus/{menu_id}/submenus/{sub_id}/dishes/{dish_id}',status_code=200)
def get_one_dishes(dish_id: str, db: Session = Depends(get_db)):
    dish = db.query(models.Dishes).filter(models.Dishes.target_dishes_id == dish_id).first()
    if not dish:
        raise HTTPException(status_code=404, detail='dish not found')
    return {'id': dish.target_dishes_id, 'title': dish.target_dishes_title, "description": dish.target_dishes_description,
            'price': dish.target_dishes_price}


# Update dishes

@router.patch('/api/v1/menus/{menu_id}/submenus/{sub_id}/dishes/{dish_id}')
def update_dishes(dish_id: str, item: Dishes, db: Session = Depends(get_db)):
    dishes_model = db.query(models.Dishes).filter(models.Dishes.target_dishes_id == dish_id).first()
    dishes_model.target_dishes_title = item.title
    dishes_model.target_dishes_description = item.description
    dishes_model.target_dishes_price = item.price
    db.add(dishes_model)
    db.commit()
    db.refresh(dishes_model)
    return item


# Delete dishes

@router.delete('/api/v1/menus/{menu_id}/submenus/{sub_id}/dishes/{dish_id}')
def delete_dishes(dish_id: str, db: Session = Depends(get_db)):
    db.query(models.Dishes).filter(models.Dishes.target_dishes_id == dish_id).delete()
    db.commit()
    return "Success"