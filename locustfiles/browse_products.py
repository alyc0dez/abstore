from locust import HttpUser, task, between

class WebSiteUser(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def view_products(self):
        self.client.get('/store/products/?collection_id=1', name='/store/products')


    @task(4)
    def view_products(self):
        product_id = 1
        self.client.get(f'/store/products/{product_id}', name='/store/products/:id')


    @task(1)
    def add_to_cart(self):
        product_id = 1
        self.client.post(
            f'/store/carts/{self.cart_id}/items/',
            name = 'sotre/carts/items',
            json={'product_id': product_id, 'quantity': 1}
        )

    def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id']

        
