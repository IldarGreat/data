# --- простая визуализация YOLO-детекций ---
import cv2

img_draw = cv2.imread(IMG)
h, w = img_draw.shape[:2]

# допустим, YOLO выдаёт (1, N, 6): [x, y, w, h, conf, class]
# или (1, N, 85) для COCO (где 5 + 80 классов)
out = np.array(outputs[0])
out = out.reshape(-1, out.shape[-1])

# фильтруем по вероятности
for det in out:
    conf = det[4]
    if conf < 0.4:  # можно подправить порог
        continue
    x, y, bw, bh = det[:4]
    # нормализованные координаты → в пиксели
    x1 = int((x - bw/2) * w)
    y1 = int((y - bh/2) * h)
    x2 = int((x + bw/2) * w)
    y2 = int((y + bh/2) * h)
    cv2.rectangle(img_draw, (x1, y1), (x2, y2), (0,255,0), 2)
    cv2.putText(img_draw, f'{conf:.2f}', (x1, y1-5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

cv2.imshow("Detections", img_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()

