import { Box, useTheme } from "@mui/material";

type SecondaryDrawProps = {
  children: React.ReactNode;
}

const SecondaryDraw = ({ children }: SecondaryDrawProps) => {
  const theme = useTheme();

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
      {children}
    </Box>
  );
};
export default SecondaryDraw;
