import typing

class Rsi:
    def get_rsi(self, data: typing.List[float or int], window_length: int,
                    use_rounding: bool = True) -> typing.List[typing.Any]:
        do_round = lambda x: round(x, 2) if use_rounding else x  # noqa: E731
        gains: typing.List[float] = []
        losses: typing.List[float] = []
        prev_avg_gain: float or None = None
        prev_avg_loss: float or None = None
        for i, price in enumerate(data):
            if i == 0:
                continue
            difference = do_round(data[i] - data[i - 1])
            if difference > 0:
                gain = difference
                loss = 0
            elif difference < 0:
                gain = 0
                loss = abs(difference)
            else:
                gain = 0
                loss = 0
            gains.append(gain)
            losses.append(loss)
            if i < window_length:
                continue
            if i == window_length:
                avg_gain = sum(gains) / len(gains)
                avg_loss = sum(losses) / len(losses)
            else:
                avg_gain = (prev_avg_gain * (window_length - 1) + gain) / window_length
                avg_loss = (prev_avg_loss * (window_length - 1) + loss) / window_length
            avg_gain = do_round(avg_gain)
            avg_loss = do_round(avg_loss)
            prev_avg_gain = avg_gain
            prev_avg_loss = avg_loss
            rs = do_round(avg_gain / avg_loss)
            rsi = do_round(100 - (100 / (1 + rs)))
            gains.pop(0)
            losses.pop(0)
        return rsi