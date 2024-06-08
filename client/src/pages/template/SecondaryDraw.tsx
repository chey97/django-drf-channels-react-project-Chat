import {
  Box,
  Drawer,
  Typography,
  useMediaQuery,
  useTheme,
} from "@mui/material";
import { useEffect, useState } from "react";

const SecondaryDraw = () => {
  const theme = useTheme();
  const below600 = useMediaQuery("(max-width:599px)");
  const [open, setOpen] = useState(true);

  useEffect(() => {
    setOpen(!below600);
  }, [below600]);

  if (below600) return null;

  return (
    <Drawer
      open={open}
      variant={"permanent"}
      PaperProps={{
        sx: {
          mt: `${theme.primaryAppBar.height}px`,
          ml: `${theme.primaryDraw.width}px`,
          height: `calc(100vh - ${theme.primaryAppBar.height})px`,
          width: theme.secondaryDraw.width,
        },
      }}
    >
      <Box>
        <Box>
          {[...Array(100)].map((_, i) => (
            <Typography key={i} paragraph>
              {i + 1}
            </Typography>
          ))}
        </Box>
      </Box>
    </Drawer>
  );
};
export default SecondaryDraw;
