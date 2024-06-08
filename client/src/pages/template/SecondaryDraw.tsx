import { Box, Typography, useTheme } from "@mui/material";
import axios from "axios";

const SecondaryDraw = () => {
  const theme = useTheme();

  axios
    .get("http://127.0.0.1:8000/api/server/select/?category=cat1")
    .then((respose) => {
      console.log(respose.data);
    })
    .catch((error) => {
      console.log(error);
    });

  return (
    <Box
      sx={{
        minWidth: `${theme.secondaryDraw.width}px`,
        height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
        mt: `${theme.primaryAppBar.height}px`,
        borderRight: `1px solid ${theme.palette.divider}`,
        display: { xs: "none", sm: "block" },
        overflowY: "auto",
        overflowX: "hidden",
      }}
    >
      {[...Array(100)].map((_, i) => (
        <Typography key={i} paragraph>
          {i + 1}
        </Typography>
      ))}
    </Box>
  );
};
export default SecondaryDraw;
