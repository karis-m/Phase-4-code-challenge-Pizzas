import { Routes, Route } from "react-router-dom";
import Header from "./Header";
import Restaurant from "./Restaurant";
import Home from "./Home";
import RestaurantPizzaForm from "./RestaurantPizzaForm";
import Pizza from "./Pizza";

function App() {
  return (
    <div>
      <Header />
        <Routes>
          <Route path="/restaurant_pizzas/new" element={<RestaurantPizzaForm />} />
          <Route exact path="/pizzas/:id" element={<Pizza />} />
          <Route exact path="/restaurants/:id" element={<Restaurant />} />
          <Route exact path="/" element={<Home />} />
        </Routes>
    </div>
  );
}

export default App;
