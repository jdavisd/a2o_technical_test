import React, { useState } from 'react';
import { Typography, Box, Container, Paper, Stack } from '@mui/material';
import { problem2 } from '../services/services';
function Problem2Page() {
  const [text, setText] = useState('');
  const [response, setResponse] = useState('')
  const handleChange = (event) => {
    setText(event.target.value);
    problem2({ input: event.target.value }).then((data) => {
      setResponse(data.response);
    }).catch((error) => {
      console.error(error);
    });;
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
            Problem 2
          </Typography>
          <Stack spacing={4}>
          <textarea value={text} align="center"id='input-2' onChange={handleChange} />
          <pre id='output-2'>{response}</pre>
          </Stack>
        </Paper>
      </Container>
    </Box>
  );
}

export default Problem2Page;