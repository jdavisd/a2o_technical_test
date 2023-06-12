import './App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Problem1Page from './pages/Problem1Page';
import Problem2Page from './pages/Problem2Page';
function App() {
  return (
    <BrowserRouter>     
        <Routes>
          <Route
            path="/problem-1"
            element={
         <Problem1Page />
            }
          />
          <Route
            path="/problem-2"
            element={
      <Problem2Page />
            }
          />
        </Routes>
  </BrowserRouter>

  );
}

export default App;
