import {
  createBrowserRouter,
} from "react-router-dom";
import Main from "../layout/Main";
import Home from "../pages/home/Home";
import Faculties from "../pages/faculties/Faculties";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Main/>,
    children: [
        {
          path: '/',
          element: <Home/>
        },
        {
          path: '/faculties',
          element: <Faculties/>
        }
    ]
  },
]);

export default router;