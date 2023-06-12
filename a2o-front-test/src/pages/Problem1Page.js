import React, { useState } from "react";
import { Typography, Box, Container, Paper, Stack } from "@mui/material";
import { problem1 } from "../services/services";
function Problem1Page() {
  const [text, setText] = useState("");
  const [response, setResponse] = useState("");
  
  const handleChange = (event) => {
    setText(event.target.value)
    const input = event.target.value;
    const inputArr = input.split(/\n| /g).map((str) => parseInt(str)).filter((value) => !Number.isNaN(value));
    
    if (inputArr.length > 3) {
      const obstacles = [];
      
      if (inputArr[1] > 0) {
        for (let i = 4; i < inputArr.length; i += 2) {
          obstacles.push([inputArr[i], inputArr[i + 1]]);
        }
      }
      
      if (inputArr[1] === obstacles.length) {
        problem1({
          n: inputArr[0],
          k: inputArr[1],
          rq: inputArr[2],
          cq: inputArr[3],
          obstacles: obstacles,
        })
          .then((data) => {
            setResponse(data.message);
          })
          .catch((error) => {
            console.error(error);
          });
      }
    }
  };
  
  return (
    <Box>
      <Container maxWidth="sm" sx={{ p: 2 }}>
        <Paper elevation={10} sx={{ p: 5, mt: 5 }}>
          <Typography
            sx={{ mb: 2 }}
            color="primary"
            variant="h5"
            component="h2"
            align="center"
          >
            Problem 1
          </Typography>
          <Stack spacing={2}>
          <textarea  style={ { height: '12em'}}align="center"value={text} id="input-1" onChange={handleChange} />
          <pre id="output-1">{response}</pre>
          </Stack>

        </Paper>
      </Container>
    </Box>
  );
}

export default Problem1Page;
