import { BrowserRouter, Route, RouterProvider, createBrowserRouter, createRoutesFromElements} from "react-router-dom";
import Home from "./pages/Home";
import React from "react";


const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>
      <Route path="/" element={<Home/>}/>
    </Route>
  )
)

const App = () => {
  return <RouterProvider router={router} />;
}

export default App;
