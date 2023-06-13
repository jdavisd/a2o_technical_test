import API from "../conection/conection";
export const problem1 = async (values)=>{
        try {
          const problem1 = await API.post (
            "/problem-1/",values
          );
          return problem1.data;
        } catch (e) {
          throw new Error(e);
        }
     
}
export const problem2 = async (values)=>{
    try {
        const problem2 = await API.post (
          "/problem-2/",values
        );
        return problem2.data;
      } catch (e) {
        throw new Error(e);
      }
}