import { Box, Typography } from "@mui/material";

type Props = {
  open: boolean;
};

const PopularChannels: React.FC<Props> = ({ open }) => {
  return (
    <>
      <Box
        sx={{
          height: 50,
          p: 2,
          diplay: "flex",
          alignItems: "center",
          flex: "1 1 100%",
        }}
      >
        <Typography sx={{ display: open ? "block" : "none" }}>
          Popular
        </Typography>
      </Box>
    </>
  );
};

export default PopularChannels;
