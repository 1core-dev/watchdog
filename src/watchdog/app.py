from fastapi import FastAPI
from .api import router

tags_metadata = [
    {
        'name': 'Authentication',
        'description': 'Users authentication'
    },
    {
        'name': 'Operations',
        'description': 'CRUD functionality of user\'s operations'
    },
    {
        'name': 'Reports',
        'description': 'Import/export .csv reports'
    }
]

app = FastAPI(
    title='Watchdog API',
    description='Personal funds flow watchdog with import/export reports feature',
    version='0.0.1',
    openapi_tags=tags_metadata
)
app.include_router(router)
