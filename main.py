from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items1/")
async def read_items(q: str | None = Query(None, min_length=3, max_length=50)):
    """q is Optional"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items2/")
async def read_items(q: str = Query("fixedquery", min_length=3)):
    """q has default value "fixedquery"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items3/")
async def read_items(q: str = Query(..., min_length=3)):
    """q is mandatory with no default value"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items4/")
async def read_items(q: list[str] = Query(["foo", "bar"])):
    """q is a list with ['foo', 'bar'] as default value"""
    query_items = {"q": q}
    return query_items

@app.get("/items5/")
async def read_items(
    q: str
    | None = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    """Additiona; metadata with q"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items6/")
async def read_items(q: str | None = Query(None, alias="item-query")):
    """q is sent as ?item-query in url"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
